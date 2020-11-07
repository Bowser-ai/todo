<template>
  <div class='root'>
      <ul>
        <li class="todocards" v-for="todoCard in todoCards" :key="todoCard.id">
          <todo-card v-bind="todoCard"></todo-card>
        </li>
      </ul>
      <button class="add_todo_card_btn" @click="addTodoCard">Nieuwe todo aanmaken</button>
    </div>
</template>

<script>
  import TodoCard from './TodoCard';
  export default {
    components: {
      'todo-card': TodoCard
    },
    data() {
      return {
        todoCards: []
      };
    },
    mounted() {
      this.retrieveAllCards()
    },
    methods: {
      async retrieveAllCards() {
        const axios = require('axios');
        const {data} = await axios.get('http://127.0.0.1:8000/todos/')
        this.todoCards = data['todo_cards'];
      },
      async addTodoCard() {
          console.log('lekker');
      }
    }
  }
</script>
<style scoped>
  .todocards {
    list-style: none;
  }
  .root {
    position: relative;
  }
  .add_todo_card_btn {
    position: relative;
    bottom: -200px;
    background-color: blue;
  }
</style>
