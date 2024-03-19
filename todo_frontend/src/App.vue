<template>
  <div id="app">
        <!-- TaskForm component -->
    <task-form ref="taskForm" @add="addTask" @edit="editTask" />
        <!-- TaskList component -->
    <task-list :tasks="tasks" @edit="setTask" @delete="deleteTask" />
  </div>
</template>

<script>
import axios from 'axios';
import TaskForm from './components/TaskForm.vue';
import TaskList from './components/TaskList.vue';

export default {
    // Components used in this Vue app

  components: {
    TaskForm,
    TaskList,
  },
  data() {
    return {
      tasks: [], // Array to store tasks
    };
  },
    // Lifecycle hook: Fetch tasks when the component is mounted
  mounted() {
    this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
          // Method to fetch tasks from the backend API
      const response = await axios.get('http://localhost:8000/api/todos/');
      this.tasks = response.data;
    },
        // Method to add a new task

    async addTask(task) {
      await axios.post('http://localhost:8000/api/todos/', task);
      this.fetchTasks();
    },
        // Method to edit a specific task

    async editTask(task) {
      await axios.put(`http://localhost:8000/api/todos/${task.id}/`, task);
      this.fetchTasks();
    },
        // Method to delete a task

    async deleteTask(taskId) {
      await axios.delete(`http://localhost:8000/api/todos/${taskId}/`);
      this.fetchTasks();
    },
        // Method to set the task in TaskForm for editing

    setTask(task) {
      this.$refs.taskForm.setTask(task);
    },
  },
};
</script>