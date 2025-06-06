function addTask() {
  const input = document.getElementById('taskInput');
  const task = input.value;

  if (!task) return;

  fetch('http://<EC2_PUBLIC_IP>:5000/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: task })
  })
  .then(res => res.json())
  .then(data => {
    input.value = '';
    fetchTasks();
  });
}

function fetchTasks() {
  fetch('http://<EC2_PUBLIC_IP>:5000/tasks')
    .then(res => res.json())
    .then(tasks => {
      const list = document.getElementById('taskList');
      list.innerHTML = '';
      tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        list.appendChild(li);
      });
    });
}

document.addEventListener('DOMContentLoaded', fetchTasks);