import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import path from "path";
import copy from 'rollup-plugin-copy'


const APPNAME = "app"
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    copy({
      targets: [
        {
          src: path.join(__dirname, "node_modules", "@viur", "shoelace", "dist", "assets"),
          dest: path.join(__dirname, 'public', "shoelace")
        }
      ]
    }),
    vue({
      template: {
        compilerOptions: {
          isCustomElement: tag => tag.startsWith('sl-')
        }
      }
    })],
  css: {
    preprocessorOptions: {
    }
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },
  server: {
    fs: {
      allow: ['/'],
    },
  },

  base:"/"+APPNAME,
  build: {
    //emptyOutDir:true,
    //target:['esnext'],
    outDir: path.resolve(__dirname, '../../deploy/'+APPNAME),
    assetsInlineLimit: 0,
    chunkSizeWarningLimit: 700,
    rollupOptions: {
      input: {
          index: path.resolve(__dirname, 'main.html'),
      },
      output: {
        chunkFileNames: (chunkinfo) => {
          if (chunkinfo['moduleIds'].filter(x => x.includes('node_modules/@viur/shoelace/dist/components')).length > 0) {
            return `[name].js`
          } else {
            return `[name]-[hash].js`
          }

        },
        manualChunks(id) {
          if (id.includes('node_modules/@viur/shoelace/dist/components')) {
            return "shoelace/component_" + id.split("/").slice(-2)[0];
          }
          if(id.includes("node_modules/@viur/ckeditor5-build-classic/build/ckeditor.js")){
            return "viur-ckeditor.js"

          }
        }
      }
  }


  }


})
