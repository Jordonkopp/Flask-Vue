<!-- components/Login.vue -->
<template>
  <div class="login-wrapper border border-light">
    <b-navbar toggleable="md" type="dark" variant="info" class="navbar">
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

        <b-navbar-brand href="#">Key-Logger</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">


          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">

          <button class="btn btn-danger navbar-btn"
              @click="go_to_register">Register</button>
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    <form class="form-signin">
      <h2 class="form-signin-heading">Sign in</h2>
      <p class="subtitle error-msg">{{ errorMsg }}</p>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input v-model="email" type="email" id="inputEmail"
             class="form-control" placeholder="Email address" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input v-model="password" type="password" id="inputPassword"
             class="form-control" placeholder="Password" required>
      <button class="btn btn-lg btn-success btn-block" type="submit"
              @click="authenticate">Sign in</button>

    </form>


  </div>
</template>

<script>

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    authenticate() {
      this.$store.dispatch('login', { email: this.email, password: this.password })
        .then(() => this.$router.push('/keys'));
    },
    go_to_register() {
      this.$router.push('/register');
    },
  },
};
</script>

<style lang="css">

body {
  border: 0;
  height: 100%;
  width: 100%;
}

.login-wrapper {
  background: #605B56;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  border: 0;
}

.form-signin {
  max-width: 330px;
  padding: 10% 15px;
  margin: 0 auto;
}
.form-signin .form-signin-heading,
.form-signin .checkbox {
  margin-bottom: 10px;
  vertical-align: middle;
  text-align: center;
}
.form-signin .checkbox {
  font-weight: normal;
}
.form-signin .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
