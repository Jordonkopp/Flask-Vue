import Vue from 'vue';
import Router from 'vue-router';
import Keys from '@/components/Keys';
import Login from '@/components/Login';
import Register from '@/components/Register';
import store from '@/store';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'base',
      component: Register,
    },
    {
      path: '/keys',
      name: 'Keys',
      component: Keys,
      beforeEnter(to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login');
        } else {
          next();
        }
      },
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
    },

  ],
  mode: 'hash',
});

