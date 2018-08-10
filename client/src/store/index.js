import Vue from 'vue';
import Vuex from 'vuex';

// imports of AJAX functions will go here
import { authenticate, register } from '@/api';
import { isValidJwt } from '@/utils';

Vue.use(Vuex);

const state = {
  // single source of data
  keys: [],
  user: {},
  jwt: '',
};

const actions = {
  // asynchronous operations
  login(context, userData) {
    context.commit('setUserData', { userData });
    return authenticate(userData)
      .then(
        response => context.commit('setJwtToken', { jwt: response.data }),
      )
      .catch((error) => {
        // eslint-disable-next-line
        console.log('Error Authenticating: ', error);
        // TODO: use eventBus to trigger warnings
      });
  },
  register_user(context, userData) {
    context.commit('setUserData', { userData });
    return register(userData)
      .then(
        response => context.commit('setJwtToken', { jwt: response.data }),
      )
      .catch((error) => {
        // eslint-disable-next-line
        console.log('Error Registering: ', error);
        // TODO: use eventBus to trigger warnings
      });
  },
  logout(context) {
    context.commit('clearJwtToken');
  },
};

const mutations = {
  // eslint-disable-next-line
  setUserData(state, payload) {
    state.userData = payload.userData;
  },
  // eslint-disable-next-line
  setJwtToken(state, payload) {
    // saving jwt to local storage
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
  // eslint-disable-next-line
  clearJwtToken(state) {
    // saving jwt to local storage
    window.localStorage.removeItem('token');
    localStorage.token = '';
    state.jwt = '';
  },
};

const getters = {
  // reusable data accessors
  // eslint-disable-next-line
  isAuthenticated(state) {
    const valid = isValidJwt(window.localStorage.getItem('token'));
    if (valid === true) {
      state.jwt = window.localStorage.getItem('token');
    }
    return valid;
  },
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
