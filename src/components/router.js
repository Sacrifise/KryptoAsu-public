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
        path: "/nok",
        name: "Nok",
        component: Nok,
        props: {page: 1}
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