<template>
  <tr class="todo-card" :id="id">
    <td>{{ name }}</td>
    <td>{{ description }}</td>
    <td>{{ retrieveDateCreated }}</td>
    <td>{{ retrieveHoursLeft}}</td>
    <td> {{ mapCompletedToStatus }}</td>
    <div role="button" class="complete" @click="completedCard">Afronden</div>
    <i role="button" @click="changeCard" class="fas fa-pencil-alt"></i>
    <i role="button" @click="removeTodoCard" class="fas fa-trash" style="margin-left: 10px"></i>
  </tr>
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
  data() {
    return {
      todoCompleted: this.completed
    };
  },
  computed: {
    retrieveDateCreated() {
      return /\d+-\d+-\d+/.exec(this.date_created)[0];
    },
    retrieveHoursLeft() {
      return /\d{2}:\d{2}/.exec(this.time_left)[0];
    },
    mapCompletedToStatus() {
      return this.todoCompleted ? 'Voltooid': 'Todo';
    }
  },
  methods : {
    async completedCard(e) {
      const axios = require('axios');
      const config = {
        method: 'PUT',
        url: 'http://127.0.0.1:8000/todos/',
        headers : {'Content-Type': 'application/json',
                   'X-CSRFToken': "",},
        data: JSON.stringify({'id':e.target.parentNode.id, 'completed': true})
      }
      const response = await axios(config);
      if (response.status === 201){
        this.todoCompleted = true;
        this.crossOutCard();
        this.$emit('completedCard');
      }
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
    },
    changeCard() {
      this.$emit('changedCard', this.id);
    },
    crossOutCard() {
      const todoCardElement = document.querySelector('[id="' + this.id + '"]');
      todoCardElement.style.textDecoration = 'line-through';
    },
  },
  mounted() {
    if (this.completed) this.crossOutCard();
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
.complete {
  color: red;
  text-decoration: underline;
}
</style>
