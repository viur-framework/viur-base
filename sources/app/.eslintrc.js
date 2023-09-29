module.exports = {
    root: true,
    env: {
        node: true
    },
    'extends': [
        'plugin:vue/vue3-essential',
        'eslint:recommended'
    ],
    parserOptions: {
        parser: 'babel-eslint'
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-unused-vars': 'off',
        'no-empty': 'off',
        'vue/no-unused-components': 'off',
        'vue/no-deprecated-slot-attribute': 'off', //Webcomponents use slot attribute
        "no-unreachable":"off"
    }
}
