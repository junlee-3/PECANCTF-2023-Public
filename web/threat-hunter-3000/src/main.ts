import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import FontAwesomeIcon from './tools/fontawesome'

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);
router.isReady().then(() => {
    app.mount('#app');
});