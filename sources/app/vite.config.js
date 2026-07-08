import path from "path";
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import copy from "@guanghechen/rollup-plugin-copy"
import VueDevTools from 'vite-plugin-vue-devtools'

// https://vitejs.dev/config/

const APPNAME = "app"
console.log(path.join("..", "..", "deploy", 'static', APPNAME, "*"))
export default defineConfig(({command, mode}) => {
    let conf = {
        plugins: [
            copy({
              targets: [
                {
                  src: path.join(__dirname, "node_modules", "@viur", "shoelace", "dist", "assets"),
                  dest: path.join(__dirname, "public", "shoelace"),
                },
              ],
            }),
            vue({
                template: {
                    compilerOptions: {
                        isCustomElement: tag => tag.startsWith('sl-') || tag.startsWith('wa-'),
                        module: "es2023",
                        target: "es2023",
                        sourceMap: true,
                    }
                }
            }),
            VueDevTools()
        ],
        resolve: {
            alias: {
                "@": path.resolve(__dirname, "./src")
            }
        },
        base: `/${APPNAME}`,
        build: {
            "outDir": "../../deploy/" + APPNAME,
            "assetsInlineLimit": 0,
            "chunkSizeWarningLimit": 700,
            rollupOptions: {
                input: {
                  index: path.resolve(__dirname, "index.html"),
                },
                output: {
                  chunkFileNames: (chunkinfo) => {
                    if (
                      chunkinfo["moduleIds"].filter((x) => x.includes("node_modules/@viur/shoelace/dist/components")).length > 0
                    ) {
                      return `[name].js`
                    } else {
                      return `[name]-[hash].js`
                    }
                  },
                  manualChunks(id) {
                    if (id.includes("node_modules/@viur/shoelace")) {
                      return "shoelace"
                    }
                    if (id.includes("node_modules/vue")) {
                      return `vue/${id.split("node_modules/")[1]}`
                    }
                    if (id.includes("node_modules/@ckeditor/ckeditor5-editor-classic/build/editor-classic.js")) {
                      return "ckeditor.js"
                    }
                  },
                }
            }
        }
    }

    return conf
})
