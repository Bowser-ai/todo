<template>
  <div class='root'>
    <p class="time-total"> Totaal aantal uren: {{ total_hours }}</p>
      <ul class="todocards">
        <li class="todocard" v-for="todoCard in todoCards" :key="todoCard.id">
          <todo-card v-bind="todoCard" @removedCard="removeCard"></todo-card>
        </li>
      </ul>
      <button class="add_todo_card_btn" @click="addTodoCard">Nieuwe todo aanmaken</button>
      <div class="modal" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
                <h5 style="margin: 0 127px" class="modal-title">Voeg een todo kaart toe</h5>
                <button type="button" class="close" @click="closeAddDialog" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p> Voer de volgende velden in</p>
              <div class="modal-body">
                <form class="todo-info">
                  <label for="activiteit">Activiteit</label>
                  <input id="activiteit" name="name">
                  <label for="omschrijving">Omschrijving</label>
                  <input id="omschrijving" name="description">
                  <label for="duur">Tijdsduur</label>
                  <input id="duur" name="time_left" placeholder="hh:mm">
                </form>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" @click="saveAddTodo">Sla op</button>
              <button type="button" class="btn btn-secondary" @click="closeAddDialog" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
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
        todoCards: [],
      };
    },
    computed: {
      total_hours() {
        return this.todoCards.reduce((acc, e) => {return acc + Number(/\d+(\d+)/.exec(e['time_left'])[1])}, 0);
      }
    },
    mounted() {
      this.retrieveAllCards()
      this.$ = window.jQuery;
    },
    methods: {
      async retrieveAllCards() {
        const axios = require('axios');
        const {data} = await axios.get('http://127.0.0.1:8000/todos/')
        this.todoCards = data['todo_cards'];
      },
      addTodoCard() {
        this.$('.modal').show();
      },
      closeAddDialog() {
        this.$('.modal').hide();
      },
      async saveAddTodo() {
        const formTodoInfo = this.$('.todo-info')
        const formData = formTodoInfo.serializeArray();
        const data_to_send = {};
        for (let fd of formData) {
          data_to_send[fd.name] = fd.value;
        }
        const axios = require('axios');
        const config = {
          method: 'POST',
          url: 'http://127.0.0.1:8000/todos/',
          headers: {'Content-Type': 'application/json'},
          data: JSON.stringify(data_to_send)
        }
        const {data} = await axios(config);
        this.addCardToUI(data);
      },
      addCardToUI(data) {
        this.todoCards = [...this.todoCards, data];
      },
      removeCard(id) {
        this.todoCards = this.todoCards.filter(e => e.id !== id);
      }
    }
  }
</script>
<style scoped>
  .todocards {
    display: flex;
    flex-wrap: wrap;
  }
  .todocard {
    list-style: none;
    margin: 20px;
  }
  .root {
    position: relative;
  }
  .add_todo_card_btn {
    position: relative;
    bottom: -200px;
    background-color: blue;
  }
  .todo-info {
    display: flex;
    flex-direction: column;
  }
</style>
