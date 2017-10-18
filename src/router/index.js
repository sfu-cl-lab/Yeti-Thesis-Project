import Vue from 'vue'
import Router from 'vue-router'
import Data from '@/components/Data'
import Debug from '@/components/Debug'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Data',
      component: Data
    }, {
      path: '/debug',
      name: 'debug',
      component: Debug
    }
  ]
})
