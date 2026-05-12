import { defineStore } from "pinia";
import { ref, reactive, computed } from "vue";
import { Request } from "@viur/vue-utils";
//import Utils, { isEmpty } from "@/utils";
//import config from "@/config.js";

export const useAccessabilityStore = defineStore("accessability", () => {
  // State
  const state = reactive({
    cursorSize: "default",
    fontSize: 0,
    lineHeight: 0,
    linksHighlighted: false,
    fontFamily: "default",
    contrastMode: "default",
    hideImages: false,
    textAlign: "default",
    currentLanguage: "de",
    infoHints: false
  });


  // Return all state, getters, and actions
  return {
    // State
    state
  };
},
  {
    persist: true
  }
);
