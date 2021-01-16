<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Secrets
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/profile/secrets/add">Add secret</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="secrets">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.login }}</td>
        <td>{{ props.item.password }}</td>
        <td>
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-profile-secrets-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { ISecret } from '@/interfaces';
import { readSecrets } from '@/store/main/getters';
import { dispatchGetSecrets } from '@/store/main/actions';

@Component
export default class Secrets extends Vue {
  public headers = [
    {
      text: 'Login',
      sortable: true,
      value: 'login',
      align: 'left',
    },
    {
      text: 'Password',
      sortable: true,
      value: 'password',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
    },
  ];
  get secrets() {
    return readSecrets(this.$store);
  }

  public async mounted() {
    await dispatchGetSecrets(this.$store);
  }
}
</script>
