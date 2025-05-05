import Nod from "./screens/Nod.vue";
import Nok from "./screens/Nok.vue";
import Abs from "./screens/Abs.vue";
import { createRouter, createWebHistory } from "vue-router";
import Recent from "./screens/Recent.vue";
import Atbash from "./screens/Atbash.vue";
import Caesar from "./screens/Caesar.vue";
import Polibius from "./screens/Polibius.vue";
const routes = [
    {
        path: "/",
        name: "App",
        component: false
    },
    {
        path: "/atbash",
        name: "Atbash",
        component: Atbash
    },
    {
        path: "/caesar",
        name: "Caesar",
        component: Caesar
    },
    {
        path: "/polibius",
        name: "Polibius",
        component: Polibius
    },
    {
        path: "/nok",
        name: "Nok",
        component: Nok,
    },
    {
        path: "/nod",
        name: "Nod",
        component: Nod,
    },
    {
        path: "/abs",
        name: "Abs",
        component: Abs,
    },
    {
        path: "/recent",
        name: "Recent",
        component: Recent,
    },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router