// frontend/vite.config.js
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      // ここがポイント！ `/api` を Laravel に転送
      '/api': {
        target: 'http://localhost:8000', // Laravel の URL
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '/api'),
      }
    }
  }
})
