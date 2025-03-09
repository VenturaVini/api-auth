// Exibir mensagens amigáveis na tela
function showMessage(message, type = 'success') {
    const msgDiv = document.createElement('div');
    msgDiv.className = `p-3 my-2 text-white rounded text-center ${type === 'error' ? 'bg-red-500' : 'bg-green-500'}`;
    msgDiv.textContent = message;
    document.body.prepend(msgDiv);
    setTimeout(() => msgDiv.remove(), 3000);
}

// Função para tratar o login
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    fetch('http://localhost:7200/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.access_token) {
            showMessage('Login bem-sucedido!', 'success');
            localStorage.setItem('access_token', data.access_token);
        } else {
            showMessage('Erro no login: ' + JSON.stringify(data), 'error');
        }
    })
    .catch(error => showMessage('Erro ao fazer login: ' + error, 'error'));
});

// Função para tratar o cadastro
document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    fetch('http://localhost:7200/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => response.json())
    .then(data => showMessage('Cadastro bem-sucedido!', 'success'))
    .catch(error => showMessage('Erro no cadastro: ' + error, 'error'));
});

// Função para tratar a alteração de senha
document.getElementById('change-password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('change-username').value;
    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;

    fetch('http://localhost:7200/auth/change_password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: currentPassword, nova_senha: newPassword })
    })
    .then(response => response.json())
    .then(data => showMessage('Senha alterada com sucesso!', 'success'))
    .catch(error => showMessage('Erro ao alterar senha: ' + error, 'error'));
});
