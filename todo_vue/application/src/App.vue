<template>
  <div id="app">
    <h1>Todo's</h1>
    <TodoCards></TodoCards>
  </div>
</template>

<script>
import TodoCards from './components/TodoCards';
export default {
  name: 'App',
  components: {
    TodoCards
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
