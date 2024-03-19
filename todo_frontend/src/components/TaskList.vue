<template>
  <div>
    <h2 style="font-family: 'Open Sans', sans-serif; font-size: 24px; color: #333;">Tasks List</h2>
        <!-- List of tasks -->
    <ul>
        <!-- Iterate over tasks and display each task item -->
      <li v-for="task in tasks" :key="task.id" class="task-item">
        <div class="task-info">
         <!-- Details of a task : title, description, and due date -->
          <div class="task-details">
            <span class="task-title">{{ task.title }}</span><br>
            <span class="task-description">{{ task.description }}</span><br>
            <span class="task-due-date">{{ task.due_date }}</span>
          </div>
            <!-- Task status section -->
          <div class="task-status">
            Status: <span class="status">{{ task.status }}</span>
          </div>
        </div>
        <!-- edit and delete buttons-->         
        <div class="task-buttons">
          <button @click="editTask(task)" class="btn-edit">Edit</button>
          <button @click="deleteTask(task.id)" class="btn-delete">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
      // Prop to receive tasks array from the parent component
  props: ['tasks'],
  methods: {
    // Method to call the edit / delete event when the edit / delete button is clicked
    editTask(task) {
      this.$emit('edit', task);
    },
    deleteTask(taskId) {
      this.$emit('delete', taskId);
    },
  },
};
</script>

<style scoped>
.task-item {
  margin-bottom: 15px;
  padding: 15px;
  border: 1px solid #938d8d;
  border-radius: 4px;
  background-color: #fbf7f7;
  display: flex;
  justify-content: space-between;
}

.task-info {
  flex: 1;
}

.task-details {
  margin-bottom: 5px;
}

.task-title {
  font-weight: bold;
  color: #333;
}

.task-status {
  color: #666;
}

.task-buttons {
  display: flex;
  align-items: center;
}

.btn-edit,
.btn-delete {
  background-color: #3498db;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 8px;
}

.btn-delete {
  background-color: #e74c3c;
}

.btn-edit:hover,
.btn-delete:hover {
  background-color: #2c3e50;
}
</style>
