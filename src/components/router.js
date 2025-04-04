import Nod from "./screens/Nod.vue";
import Nok from "./screens/Nok.vue";
import Abs from "./screens/Abs.vue";
import { createRouter, createWebHistory } from "vue-router";
import Recent from "./screens/Recent.vue";

const routes = [
    {
        path: "/",
        name: "App",
        component: false
    },
    {
        path: "/atbash",
        name: "Atbash",
        component: Recent
    },
    {
        path: "/caesar",
        name: "Caesar",
        component: Recent
    },
    {
        path: "/polibius",
        name: "Polibius",
        component: Recent
    },
    {
        path: "/shift",
        name: "Shift",
        component: Recent
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