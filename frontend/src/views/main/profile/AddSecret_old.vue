<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Add Secret</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Type login" type="email" v-model="login" v-validate="'required|email'" data-vv-name="email" :error-messages="errors.collect('email')" required></v-text-field>
            <v-layout align-center>
              <v-flex>
                <v-text-field type="Type password" ref="password" label="Set Password" data-vv-name="password" data-vv-delay="100" v-validate="{required: true}" v-model="password" :error-messages="errors.first('password')">
                </v-text-field>
              </v-flex>
            </v-layout>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid">
              Save
            </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {
  IAddSecret,
} from '@/interfaces';
import { dispatchAddSecret, dispatchGetSecrets } from '@/store/main/actions';

@Component
export default class AddSecret extends Vue {
  public valid = false;
  public login: string = '';
  public password: string = '';

  public async mounted() {
    await dispatchGetSecrets(this.$store);
    this.reset();
  }

  public reset() {
    this.login = '';
    this.password = '';
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedSecret: IAddSecret = {
        login: this.login,
      };
      updatedSecret.password = this.password;
      await dispatchAddSecret(this.$store, updatedSecret);
      this.$router.push('/main/profile/secrets');
    }
  }
}
</script>
