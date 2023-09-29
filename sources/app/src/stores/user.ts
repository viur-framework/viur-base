// @ts-nocheck
import {reactive, computed} from 'vue';
import {defineStore} from "pinia";
import {Request} from "@viur/vue-utils";
import utils from '../utils'
import {useAppStore} from "./app";
import {useRoute} from "vue-router";

const googleConfig = {
  library: "https://accounts.google.com/gsi/client",
  defaultButtonConfig: {theme: "outline", size: "large"},
  scopes: "email"
}


interface CredentialPopupResponse {
  clientId: string;
  /** JWT credential string */
  credential: string;
  /** This field shows how the credential is selected */
  select_by:
    | "auto"
    | "user"
    | "user_1tap"
    | "user_2tap"
    | "btn"
    | "btn_confirm"
    | "brn_add_session"
    | "btn_confirm_add_session";
}

interface TokenPopupResponse {
  /** The access token of a successful token response. */
  access_token: string;
  authuser: string;
  /** The lifetime in seconds of the access token. */
  expires_in: string;
  /** Type of prompt presented to the user */
  prompt: string;
  /** A space-delimited list of scopes that are approved by the user. */
  scope: string;
  /** The type of the token issued. */
  token_type: string;
}

export const useUserStore = defineStore("user", () => {
  const route = useRoute();

  const state = reactive({
    //user related
    "user": null,
    "user.loggedin": "no", // "yes", "no", "loading"
    "user.login.type": "no", // "no","user", "google", "sso"
    "favoriteModules": [],
    "lastActions": [],
    "syncedlastActions": [],
    "lastSynced": new Date().getTime(),


    //google stuff
    "google.api.loaded": false,
    "google.api.clientid": "",
    "google.api.renderButton": true,


  })

  function resetLoginInformation() {
    state["user"] = null
    state["user.loggedin"] = "no"
    state["user.login.type"] = "no"
  }

  function googleInit(ClientId: string) {
    return new Promise((resolve, reject) => {
      if (!ClientId) {
        reject("missing clientid");
        return;
      }

      state["google.api.clientid"] = ClientId
      if (!state["google.api.loaded"]) {
        const script = document.createElement("script");
        script.addEventListener("load", () => {
          state["google.api.loaded"] = true
          // @ts-ignore
          window.google.accounts.id.initialize({
            client_id: state["google.api.clientid"],
            scope: googleConfig.scopes,
            ux_mode: "popup",
            prompt_parent_id: "google_oauth",
            callback: (response: CredentialPopupResponse) => {
              if (response.credential) {
                Request.securePost("/vi/user/auth_googleaccount/login", {
                  dataObj: {"token": response.credential},
                  amount:1
                }).then((resp: Response) => {
                  Request.get("/vi/user/view/self").then(
                    async (resp: Response) => {
                      let data = await resp.json()
                      state["user.loggedin"] = "yes"
                      state["user"] = data.values
                      state["user.login.type"] = "google"
                      resolve(response);
                    }).catch(
                    (error: Error) => {
                      resetLoginInformation()
                      state["user.loggedin"] = "error"
                      reject(response);
                    })
                }).catch(
                  (error: Error) => {
                    resetLoginInformation()
                    state["user.loggedin"] = "error"
                    reject(response);
                  })
              } else {
                resetLoginInformation()
                state["user.loggedin"] = "error"
                reject(response);
              }
            }
          })
          // @ts-ignore
          resolve(window.google)

        });
        script.src = googleConfig.library
        script.async = true
        script.defer = true
        document.head.appendChild(script)
      }
    })
  }

  function googleLogin() {
    return new Promise((resolve, reject) => {
      state["user.loggedin"] = "loading"
      // @ts-ignore
      console.log(window.google.accounts)
      window.google.accounts.id.prompt((notification) => {
        if (["suppressed_by_user", "opt_out_or_no_session", "undefined"].includes(notification.getNotDisplayedReason())) {
          console.log("Please delete the g_state cookie")
          let div = document.getElementById("google_oauth")
          window.google.accounts.id.renderButton(div, {theme: 'outline', size: 'large'})

        }
      })
    });
  }

  function userLogin(name: string, password: string) {
    return new Promise((resolve, reject) => {
      state["user.loggedin"] = "loading"
      Request.securePost("/vi/user/auth_userpassword/login",
        {
          dataObj: {
            "name": name,
            "password": password
          },
          amount:1
        }
      ).then(async (respLogin: Response) => {
        const logindata = await respLogin.json()
        if (logindata === "OKAY") {
          Request.get("/vi/user/view/self").then(
            async (resp: Response) => {
              let data = await resp.json()
              state["user.loggedin"] = "yes"
              state["user"] = data.values
              state["user.login.type"] = "user"
            }).catch(
            (error: Error) => {
              resetLoginInformation()
              state["user.loggedin"] = "error"
              reject(respLogin);
            }
          )
        } else if (logindata["action"] === "authenticatorOTP")//We have a second factor
        {
          state["user.loggedin"] = "secound_factor_authenticator_otp"
          state["user.login.type"] = logindata["action"].toLowerCase()

        }


      }).catch(
        (error: Error) => {
          resetLoginInformation()
          state["user.loggedin"] = "error"
          reject(error);
        }
      )
    })
  }

  function userSecondFactor(otp: string) {
    return new Promise((resolve, reject) => {
      state["user.loggedin"] = "loading"
      Request.securePost(`/vi/user/f2_${state["user.login.type"]}/verify`, {dataObj: {"otp": otp}, amount:1})
        .then(async (resp) => {
          const opt_data= await resp.json();
          if (opt_data.errors) {
                if (opt_data.errors.length > 0) {
                  state["user.loggedin"] = "error";
                  return;
                }

              }
          Request.get("/vi/user/view/self").then(
            async (resp: Response) => {
              let data = await resp.json();



              state["user.loggedin"] = "yes"
              state["user"] = data.values
              state["user.login.type"] = "user"
            }).catch(
            (error: Error) => {
              resetLoginInformation()
              state["user.loggedin"] = "error"
              reject(resp);
            }
          )
        })
    })
  }

  function logout() {
    state["user.loggedin"] = "loading"
    if (state["user.login.type"] === "google") {
      //@ts-ignore
      //window.google.accounts.id.disableAutoSelect();
      window.google.accounts.id.revoke();
    }
    Request.securePost("/vi/user/logout").then((resp: Response) => {
        resetLoginInformation()
      }
    ).catch(
      (error: Error) => {
        resetLoginInformation()
        state["user.loggedin"] = "error"
      }
    )
  }

  function updateUser() {
    return new Promise((resolve, reject) => {

      Request.get("/vi/user/view/self").then(
        async (resp: Response) => {
          let data = await resp.json()
          state["user.loggedin"] = "yes"
          state["user"] = data.values
          state["user.login.type"] = "user"
          if (data.values["admin_config"]) {
            const obj = data.values["admin_config"];
            if (obj !== null) {
              for (const key in obj["lastActions"])//back to array
              {
                state.lastActions.push(obj["lastActions"][key]);
                state.syncedlastActions.push(obj["lastActions"][key]);
              }

            }
          }
          resolve(resp)
        }).catch(
        (error: Error) => {
          resetLoginInformation()
          reject(error);
        }
      )


    })

  }

  const getUser = computed(() => {
    if (state["user.loggedin"] === 'no') { //destroy userinfos
      state["user"] = null
      return false
    }

    return state["user"]
  })

  const userAccess = computed(() => {
    if (!state.user) return []

    return state.user["access"]
  })

  const userShortname = computed(() => {
    if (!state.user) return "-"

    if (state.user["firstname"]) {
      return `${state.user["firstname"][0]}. ${state.user["lastname"]}`
    } else {
      return state.user["lastname"]
    }
  })

  return {
    state,
    userAccess,
    userShortname,
    updateUser,
    googleInit,
    googleLogin,
    userLogin,
    userSecondFactor,
    logout
  }
})
