<template>
  <div>
<h2 style="font-family: 'Open Sans', sans-serif;">{{ editing ? 'Edit Task' : 'Add Task' }}</h2>
    <!-- Form for adding/editing tasks -->

    <form @submit.prevent="saveTask" class="task-form">
      <div class="form-group">
        <label for="title">Title:</label>
        <input id="title" v-model="task.title" required />
      </div>

      <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" v-model="task.description" required></textarea>
      </div>

      <div class="form-group">
        <label for="dueDate">Due Date:</label>
        <input type="date" id="dueDate" v-model="task.due_date" required />
      </div>

      <div class="form-group">
        <label for="status">Status:</label>
        <select id="status" v-model="task.status" required>
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Done">Done</option>
        </select>
      </div>
 <!-- The submit button -->
      <div class="form-group">
        <button type="submit" class="btn-submit">{{ editing ? 'Edit Task' : 'Add New Task' }}</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
// Data for managing the task being edited/added
  data() {
    return {
      task: {
        title: '',
        description: '',
        due_date: '',
        status: 'Pending', // Default status
      },
      editing: false,
    };
  },
  methods: {
    saveTask() {
      if (this.editing) {
        // call the edit event if in edit mode

        this.$emit('edit', this.task);
      } else {
        // call the add event if in add mode
        this.$emit('add', this.task);
      }
        // Reset the form after saving

      this.resetForm();
    },
    resetForm() {
      this.task = {
        title: '',
        description: '',
        due_date: '',
        status: 'Pending',
      };
      this.editing = false;
    },
        // Method to set the task data when in edit mode
    setTask(task) {
      this.task = { ...task };
      this.editing = true;
    },
  },
};
</script>

<style scoped>
.task-form {
  max-width: 400px;
  margin: auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input,
textarea,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #3bad6a;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #339938;
}
</style>
