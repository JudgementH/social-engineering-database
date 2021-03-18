import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import echarts from 'echarts'

Vue.use(VueAxios, axios)
Vue.config.productionTip = false
Vue.prototype.$echarts = echarts


new Vue({
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
