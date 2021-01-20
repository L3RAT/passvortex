<template>
  <div id="recaptcha2" ref="recaptchaContainer"></div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from 'vue-property-decorator';
import { appRecaptchaSiteKey } from '@/env';

function defaultSiteKey() {
  return appRecaptchaSiteKey || 'site-key-not-defined';
}

function loadRecaptcha(callback: () => void) {
  let win = window as any;
  if (win && !win.grecaptcha) {
    const recaptchaScript = document.createElement('script');
    document.head.appendChild(recaptchaScript);
    recaptchaScript.onload = () => {
      win = window as any;
      win.grecaptcha.ready(() => {
        callback();
      });
    };
    recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js');
  } else {
    callback();
  }
}

@Component
export default class extends Vue {
  @Prop({default: defaultSiteKey()}) private siteKey!: string;

  private passed: boolean = false;

  private widgetId: string|undefined = undefined;

  private get widgetCreated(): boolean {
    return this.widgetId !== undefined;
  }

  private mounted() {
    loadRecaptcha(() => this.mountRecaptcha());
  }

  private mountRecaptcha() {
    const recaptchaApi: any = (window as any).grecaptcha;
    const container = this.$refs.recaptchaContainer;
    this.widgetId = recaptchaApi.render(container, {
      'callback': () => {
        const result = recaptchaApi.getResponse(this.widgetId);
        this.passed = true;
        this.$emit('change', this.passed);
        this.$emit('passed', result); // if caller wants to test signature server-side
      },
      'expired-callback': () => {
        this.passed = false;
        this.$emit('change', this.passed);
        this.$emit('expired');
      },
      'sitekey': this.siteKey,
    });
  }
}
</script>