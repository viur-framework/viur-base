import view_missing from "../views/errors/view_missing.vue";
import {createRouter, createWebHashHistory} from "vue-router";

//define statics
const routes = [
  {
    path: '/:pathMatch(.*)*',
    name: 'view_missing',
    component: view_missing
  },
  {
    path: '/',
    name: 'home',
    component: () => import("../views/Home.vue")
  },
]


const router = createRouter({
  // @ts-ignore
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes
})

export default router
