import vue from 'eslint-plugin-vue';

export default [
  {
    files: ['src/**/*.vue'],
    languageOptions: {
      parser: await import('vue-eslint-parser'),
      parserOptions: {
        ecmaVersion: 2022,
        sourceType: 'module',
        parser: {
          js: 'espree',
        },
      },
    },
    plugins: {
      vue,
    },
    rules: {
      'vue/no-unused-components': 'warn',
      'vue/no-unused-vars': 'warn',
      // 必要に応じてルール追加
    },
  },
];
