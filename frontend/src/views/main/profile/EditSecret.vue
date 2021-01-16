<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Secret</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form
            v-model="valid"
            ref="form"
            lazy-validation
          >
            <v-text-field
              label="Login"
              v-model="login"
              v-validate="'required|email'"
              data-vv-name="email"
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
            <v-text-field
              label="Password"
              v-model="password"
              required
            ></v-text-field>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn
          @click="submit"
          :disabled="!valid"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { ISecret, ISecretUpdate } from '@/interfaces';
import { dispatchGetSecrets, dispatchUpdateSecret } from '@/store/main/actions';
import { readOneSecret } from '@/store/main/getters';

@Component
export default class EditSecret extends Vue {
  public valid = true;
  public login: string = '';
  public setPassword = false;
  public password: string = '';

  public async mounted() {
    await dispatchGetSecrets(this.$store);
    this.reset();
  }

  public reset() {
    this.setPassword = false;
    this.password = '';
    this.login = '';
    this.$validator.reset();
    if (this.secret) {
      this.login = this.secret.login;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedSecret: ISecretUpdate = {};
      if (this.login) {
        updatedSecret.login = this.login;
      }
      if (this.password) {
        updatedSecret.password = this.password;
      }
      await dispatchUpdateSecret(this.$store, { id: this.secret!.id, secret: updatedSecret });
      this.$router.push('/main/profile/secrets');
    }
  }

  get secret() {
    return readOneSecret(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
