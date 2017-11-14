<template>
  <div id="app">

    <el-menu default-active="2" mode="horizontal">
      <el-menu-item index="1">Data Visualization</el-menu-item>
      <el-menu-item index="2">
        <router-link to="/" tag="li">NHL Dataset</router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <router-link to="/ng" tag="li">General Tool (under construction)</router-link>
      </el-menu-item>
    </el-menu>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: "Noto Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
