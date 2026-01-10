// Simple Hello World CRUD using localStorage (simulating a database)

// CREATE or UPDATE
function saveHelloWorld(text) {
  localStorage.setItem('helloWorldText', text);
}

// READ
function getHelloWorld() {
  return localStorage.getItem('helloWorldText') || 'Hello World';
}

// DELETE
function deleteHelloWorld() {
  localStorage.removeItem('helloWorldText');
}

// UI Demo
window.onload = function() {
  const display = document.getElementById('display');
  display.textContent = getHelloWorld();

  document.getElementById('saveBtn').onclick = function() {
    const val = document.getElementById('input').value || 'Hello World';
    saveHelloWorld(val);
    display.textContent = getHelloWorld();
  };

  document.getElementById('deleteBtn').onclick = function() {
    deleteHelloWorld();
    display.textContent = getHelloWorld();
  };
};
