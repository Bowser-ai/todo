<template>
  <div class="todo-card">
    <p class="header">activiteit:</p>
    <p>{{ name }}</p>
    <p class="header">omschrijving:</p>
    <p>{{ description }}</p>
    <p class="header">aangemaakt op:</p>
    <p>{{ retrieve_date_created }}</p>
    <label class="header" for="time-left">nog te besteden uren:</label>
    <input id="time-left" min="0" type="number" :value="retrieve_hours_left">
    <button class="time-left-btn">Instellen tijd</button>
    <label class="header" for="completed">Voltooid? </label>
    <input id="completed" type="checkbox" style="margin: 0 auto" :checked="completed">
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    name: String,
    description: String,
    date_created: String,
    time_left: String,
    completed: Boolean
  },
  computed: {
    retrieve_date_created() {
      return /\d+-\d+-\d+/.exec(this.date_created)[0];
    },
    retrieve_hours_left() {
      return /\d+(\d+)/.exec(this.time_left)[1];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  font-weight: bold;
  font-size: 16pt;
  margin: 10px;
}
.todo-card {
  border: 1px black solid;
  border-radius: 10px;
  background-color: #0c51ce;
  width: fit-content;
  height: fit-content;
  padding: 40px;
  display: flex;
  flex-direction: column;
}
#time-left {
  margin:auto;
  width: fit-content;
  text-align: center;
}

.time-left-btn {
    width: fit-content;
    margin: 20px auto;
}
</style>
