import js from '@eslint/js'
import pluginVue from 'eslint-plugin-vue'
import pluginVitest from '@vitest/eslint-plugin'
import skipFormatting from 'eslint-config-prettier/flat'
import globals from 'globals'

export default [
  {
    ignores: ['.venv/**', 'deploy/**', 'sources/*/public/**', '**/dist/**', '**/coverage/**'],
  },

  {
    files: ['**/*.{js,mjs,cjs,vue}'],
  },

  js.configs.recommended,
  ...pluginVue.configs['flat/essential'],

  {
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      'no-unused-vars': 'warn',

      // `slot="..."` on web components (Shoelace, Web Awesome) is the native
      // HTML slot attribute, not the deprecated Vue 2 slot syntax
      'vue/no-deprecated-slot-attribute': 'off',

      // globally registered components like `Bone` are named after their domain concept
      'vue/multi-word-component-names': 'off',
    },
  },

  // build tooling runs in Node, not in the browser
  {
    files: ['*.config.{js,mjs,cjs}', 'sources/*/*.config.{js,mjs,cjs}'],
    languageOptions: {
      globals: {
        ...globals.node,
      },
    },
  },

  {
    ...pluginVitest.configs.recommended,
    files: ['sources/*/src/**/__tests__/*'],
  },

  // must stay last: turns off everything Prettier owns
  skipFormatting,
]
