import { createApp } from 'vue'
import router from './router'
import ElementPlus from 'element-plus'
import request from './request'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus)
app.use(router)

app.config.globalProperties.$http = request

app.mount('#app')
