<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
*,
*::before,
*::after {
    box-sizing: border-box;
}

html {
  font-size: 100%;
}
body {
  margin: 0px;
  width: 100%;
  height: 100vh;
}
h1, h2 {
  margin: 0px;
}
#app {
  font-family: 'Lato', sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
  height: 100vh;

}
</style>
