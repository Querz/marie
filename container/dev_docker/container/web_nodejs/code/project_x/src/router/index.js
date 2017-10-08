import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import SignIn from '@/components/SignIn'
import Profile from '@/components/Profile'
import Main from '@/components/Main'
import StepBuilder from '@/components/StepBuilder'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/stepbuildber',
      name: 'StepBuilder',
      component: StepBuilder
    }
  ]
})
