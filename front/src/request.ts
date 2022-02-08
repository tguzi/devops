import axios from 'axios'
import { ElMessage } from 'element-plus'

const instance = axios.create({
  headers: {
    'Content-Type': 'application/json;charset=UTF-8',
    'Access-Control-Allow-Origin-Type': '*'
  },
  timeout: 50000,
  baseURL: window.location.origin,
  withCredentials: true
})

instance.interceptors.request.use(
  (config) => {
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
