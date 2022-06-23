import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchLatestData from '../views/SearchLatestData.vue'
import SearchHistoryData from '../views/SearchHistoryData.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/search-latest-data',
        name: 'searchLatestData',
        component: SearchLatestData
    },
    {
        path: '/search-history-data',
        name: 'searchHistoryData',
        component: SearchHistoryData
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router