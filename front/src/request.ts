import axios from 'axios'
import qs from 'qs'
import { ElMessage } from 'element-plus'

const instance = axios.create({
  timeout: 5000,
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  // baseURL: window.location.origin,
  baseURL: 'http://127.0.0.1:8000',
  withCredentials: true
})

instance.interceptors.request.use(
  (config) => {
    if (config.method === 'post') {
      config.data = qs.stringify(config.data)
    }
    return config
  },
  (error) => {
    ElMessage({
      type: 'error',
      message: '出错了'
    })
    return Promise.reject(error)
  }
)
// 响应拦截器
instance.interceptors.response.use((response) => {
  if (response.status === 200) {
    return Promise.resolve(response.data)
  } else {
    return Promise.reject(response)
  }
})

export default instance
