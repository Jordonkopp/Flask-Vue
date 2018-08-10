<template>
  <div class="container-fluid">
      <b-navbar toggleable="md" type="dark" variant="info" class="navbar">
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

        <b-navbar-brand href="#">Key-Logger</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">


          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>User</em>
            </template>
            <b-dropdown-item @click="logout">Signout</b-dropdown-item>
          </b-nav-item-dropdown>

          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    <br><br>
    <alert :message=message v-if="showMessage"></alert>
    <button type="button" class="btn btn-success btn-sm" v-b-modal.key-modal>Add Key</button>
    <br><br>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col" id="id-header">ID</th>
          <th id="delete-header">Delete?</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(key, index) in keys" :key="index">
          <td>{{ key.key }}</td>

          <td class="delete-cell">
            <button
                    type="button"
                    class="btn btn-danger btn-sm delete-button"
                    @click="onDeleteKey(key._id)">
                Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <b-modal ref="addKeyModal"
             id="key-modal"
             title="Add a new key"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-key-group"
                    label="Key:"
                    label-for="form-key-input">
          <b-form-input id="form-key-input"
                        type="text"
                        v-model="addKeyForm.id"
                        required
                        placeholder="Enter key">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      keys: [],
      addKeyForm: {
        id: '',
      },
      editForm: {
        id: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
        .then(() => this.$router.push('/login'));
    },
    getKeys() {
      const path = 'http://localhost:5000/keys';
      axios.get(path, { headers: { Authorization: `Bearer: ${localStorage.token}` } })
        .then((res) => {
          this.keys = res.data.result.keys;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addKey(payload) {
      const path = 'http://localhost:5000/keys';
      axios.post(path, payload, { headers: { Authorization: `Bearer: ${localStorage.token}` } })
        .then(() => {
          this.getKeys();
          this.message = 'Key added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getKeys();
        });
    },
    removeKey(keyId) {
      const path = `http://localhost:5000/keys/${keyId}`;
      axios.delete(path, { headers: { Authorization: `Bearer: ${localStorage.token}` } })
        .then(() => {
          this.getKeys();
          this.message = 'Key removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getKeys();
        });
    },
    initForm() {
      this.addKeyForm.id = '';
      this.editForm.id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addKeyModal.hide();
      const payload = {
        key: this.addKeyForm.id,
      };
      this.addKey(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addKeyModal.hide();
      this.initForm();
    },
    onDeleteKey(keyId) {
      this.removeKey(keyId);
    },
  },
  created() {
    this.getKeys();
  },
};
</script>
<style lang="css">

  #id-header {
    width: 75%;
  }

  #delete-header {
    width: 75%;
  }

  .delete-cell {
    padding: 0;
  }

  .delete-button{
    width: 75%;
  }
</style>
