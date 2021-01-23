<template>
<div class="root">
  <div class="table-btn-container">
    <table class="todocard-table">
      <tr class="table-headers">
        <th>Activiteit</th>
        <th>Omschrijving</th>
        <th>Datum</th>
        <th>Uren te besteden</th>
        <th>Status</th>
      </tr>
      <todo-card v-for="todoCard in todoCards" v-bind="todoCard" @removedCard="removeCard" @changedCard="changeCard" v-bind:key="todoCard.id"></todo-card>
    </table>
    <button @click="addTodoCard" class="add-todo-card-btn">Maak Todo aan</button>
  </div>
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
      return this.todoCards.reduce((acc, e) => {
        return acc + Number(/\d+(\d+)/.exec(e['time_left'])[1])
      }, 0);
    }
  },
  mounted() {
    this.retrieveAllCards()
    this.$ = window.jQuery;
  },
  methods: {
    async retrieveAllCards() {
      const axios = require('axios');
      const {
        data
      } = await axios.get('http://127.0.0.1:8000/todos/');
      this.todoCards = data['todo_cards'];
    },
    addTodoCard() {
      this.$('.modal').show();
    },
    closeAddDialog() {
      this.$('#hidden-id-field').remove();
      this.$('.todo-info').get(0).reset();
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
        method: data_to_send.id ? 'PUT' : 'POST',
        url: 'http://127.0.0.1:8000/todos/',
        headers: {
          'Content-Type': 'application/json'
        },
        data: JSON.stringify(data_to_send)
      }
      const {
        data
      } = await axios(config);
      if (!data_to_send.id) this.addCardToUI(data);
      else this.updateCard(data);
      this.closeAddDialog();
    },
    addCardToUI(data) {
      this.todoCards = [...this.todoCards, data];
    },
    removeCard(id) {
      this.todoCards = this.todoCards.filter(e => e.id !== id);
    },
    changeCard(id) {
      const todoCard = this.todoCards.find(e => e.id === id);
      const $todoForm = this.$('.todo-info');
      this.$('.modal').show();
      const $idField = this.$('<input>', {
        id: 'hidden-id-field',
        name: 'id',
        value: todoCard.id,
        hidden: true
      });
      $todoForm.append($idField);
      $todoForm.children().each((_, element) => {
        if (element.name !== undefined) {
          element.value = todoCard[element.name];
        }
      });
    },
    updateCard(data) {
      this.todoCards = this.todoCards.map(e => {
        if (e.id === data.id) {
          return data;
        }
        return e;
      });
    }
  }
}
</script>
<style scoped>
.todocards {
  margin: 20px;
}

.todocard {
  list-style: none;
  margin: 20px;
}

.root {
  margin: 20px;
}

.add-todo-card-btn {
  background-color: #d94242;
  float: left;
  margin: 10px;
}

.todo-info {
  display: flex;
  flex-direction: column;
}

.table-headers {
  color: black;
}

.todocard-table {
  color: white;
  width: 100%;
  border-collapse: separate;
  border-spacing: 5px 5px;
  margin-top: 40px;
}
</style>
