<template>
  <div class="todo-card" :id="id">
    <p class="header">activiteit:</p>
    <p>{{ name }}</p>
    <p class="header">omschrijving:</p>
    <p>{{ description }}</p>
    <p class="header">aangemaakt op:</p>
    <p>{{ retrieve_date_created }}</p>
    <label class="header" for="time-left">nog te besteden uren:</label>
    <input id="time-left" :value="retrieve_hours_left">
    <button class="time-left-btn">Instellen tijd</button>
    <label class="header" for="completed">Voltooid? </label>
    <input id="completed" type="checkbox" style="margin: 0 auto" :checked="completed" @change="changeCompleted">
    <button class="remove-card" @click="removeTodoCard">Verwijderen</button>
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
      return /\d{2}:\d{2}/.exec(this.time_left)[0];
    }
  },
  methods : {
    changeCompleted(e) {
      const axios = require('axios');
      const config = {
        method: 'PUT',
        url: 'http://127.0.0.1:8000/todos/',
        headers : {'Content-Type': 'application/json',
                   'X-CSRFToken': "",},
        data: JSON.stringify({'id':e.target.parentNode.id, 'completed': e.target.checked})
      }
      axios(config);
    },
    async removeTodoCard() {
      const axios = require('axios');
      const data = {'id': this.id}
      const config = {
        url: 'http://127.0.0.1:8000/todos/',
        method: 'delete',
        'Content-Type': 'application/json',
        data
      }
      await axios(config);
      this.$emit('removedCard', this.id);
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
.remove-card {
  margin-top: 20px;
}
</style>
