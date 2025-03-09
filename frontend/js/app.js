// Exibir mensagens amigáveis
function showMessage(message, type = 'success') {
    const msgDiv = document.createElement('div');
    
    // Define as classes CSS de acordo com o tipo da mensagem
    msgDiv.className = `p-3 my-2 text-white rounded text-center ${type === 'error' ? 'bg-red-500' : 'bg-green-500'}`;
    
    // Atribui o texto da mensagem
    msgDiv.textContent = message;
    
    // Adiciona a mensagem no topo da página (prepend coloca no começo do body)
    document.body.prepend(msgDiv);
    
    // Remove a mensagem após 3 segundos
    setTimeout(() => msgDiv.remove(), 3000);
}


// Função para tratar o login
document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    fetch('http://localhost:7200/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => {
        if (!response.ok) { // Verifica se a resposta é um erro (status diferente de 200-299)
            return response.json().then(data => {
                throw new Error(data.detail || 'Erro desconhecido');
            });
        }
        return response.json(); // Retorna o JSON da resposta para o próximo then
    })
    .then(data => {
        if (data.access_token) {
            showMessage('Login bem-sucedido!', 'success');
            // showMessage('TOKEN', 'Bearer ' + data.access_token);
            localStorage.setItem('access_token', data.access_token);
            // Redireciona após sucesso
            window.location.href = 'menu.html';
        }
    })
    .catch(error => showMessage('Erro ao fazer login: ' + error.message, 'error'));
});


// Função para tratar o cadastro
document.getElementById('signup-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    fetch('http://localhost:7200/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => { // Captura a resposta do corpo, que contém o erro
                throw new Error(data.detail || 'Erro desconhecido'); // Usa a mensagem de erro da API
            });
        }
    })
    .then(data => {
        showMessage('Cadastro bem-sucedido!', 'success');
        // Redireciona para login após sucesso
        window.location.href = 'index.html';
    })
    .catch(error => {
        showMessage('Erro no cadastro: ' + error.message, 'error');
    });
});


// Função para tratar a alteração de senha
document.getElementById('change-password-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('change-username').value;
    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;

    fetch('http://localhost:7200/auth/change_password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: currentPassword, nova_senha: newPassword })
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Caso a resposta seja bem-sucedida (status 200)
        } else {
            return response.json().then(data => { // Captura a resposta do corpo, que contém o erro
                throw new Error(data.detail || 'Erro desconhecido'); // Usa a mensagem de erro da API
            });
        }
    })
    .then(data => showMessage('Senha alterada com sucesso!', 'success'))
    .catch(error => showMessage(error.message, 'error')); // Exibe a mensagem de erro, caso ocorra
});





// ADICIONAR PRODUTO
document.getElementById('adicionar-produto-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const produtoId = document.getElementById('produto-id').value;
    const produtoNome = document.getElementById('produto-nome').value;
    const produtoDescricao = document.getElementById('produto-descricao').value;
    const produtoPreco = document.getElementById('produto-preco').value;
    const produtoEstoque = document.getElementById('produto-estoque').value;

    // Criação do objeto produto com todos os dados
    const produto = {
        id: produtoId,
        nome: produtoNome,
        descricao: produtoDescricao,
        preco: parseFloat(produtoPreco),
        estoque: parseInt(produtoEstoque)
    };

    // Recuperando o token do localStorage
    const token = localStorage.getItem('access_token');
    
    if (!token) {
        document.getElementById('message').textContent = 'Erro: Token de acesso não encontrado!';
        return;
    }

    // Envio do produto para o back-end com o token no cabeçalho
    fetch('http://localhost:7200/produtos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`  // Inclui o token no cabeçalho
        },
        body: JSON.stringify(produto)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.detail || 'Erro desconhecido');
            });
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('message').textContent = data.mensagem || 'Produto adicionado com sucesso!';
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Erro: ' + error.message;
    });
});



//ALTERAR PRODUTO
document.getElementById('alterar-produto-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const produtoId = document.getElementById('produto-id').value;
    const produtoNome = document.getElementById('produto-nome').value;
    const produtoDescricao = document.getElementById('produto-descricao').value;
    const produtoPreco = document.getElementById('produto-preco').value;
    const produtoEstoque = document.getElementById('produto-estoque').value;

    // Criação do objeto produto com todos os dados
    const produto = {
        id: produtoId,
        nome: produtoNome,
        descricao: produtoDescricao,
        preco: parseFloat(produtoPreco),
        estoque: parseInt(produtoEstoque)
    };

    // Recuperando o token do localStorage
    const token = localStorage.getItem('access_token');
    
    if (!token) {
        document.getElementById('message').textContent = 'Erro: Token de acesso não encontrado!';
        return;
    }

    // Envio do produto para o back-end com o token no cabeçalho
    fetch('http://localhost:7200/produtos/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`  // Inclui o token no cabeçalho
        },
        body: JSON.stringify(produto)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.detail || 'Erro desconhecido');
            });
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('message').textContent = data.mensagem || 'Produto alterado com sucesso!';
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Erro: ' + error.message;
    });
});

// DELETAR PRODUTO
document.getElementById('deletar-produto-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const produtoId = document.getElementById('produto-id').value;

    // Verifica se o produtoId não está vazio
    if (!produtoId) {
        document.getElementById('message').textContent = 'Erro: ID do produto não fornecido!';
        return;
    }

    // Recuperando o token do localStorage
    const token = localStorage.getItem('access_token');
    
    if (!token) {
        document.getElementById('message').textContent = 'Erro: Token de acesso não encontrado!';
        return;
    }

    // Envio do produto para o back-end com o token no cabeçalho
    fetch(`http://localhost:7200/produtos/${produtoId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`  // Inclui o token no cabeçalho
        }
        // Caso o backend precise de um corpo para o DELETE, descomente a linha abaixo
        // body: JSON.stringify({ produtoId }) 
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.detail || 'Erro desconhecido');
            });
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('message').textContent = data.mensagem || 'Produto removido com sucesso!';
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Erro: ' + error.message;
    });
});



// Função para alternar entre o modo escuro e claro
const toggleDarkMode = () => {
    const body = document.body;
    body.classList.toggle('dark-mode');
    
    // Salvar a preferência do usuário no localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        localStorage.removeItem('dark-mode');
    }
};

// Carregar o modo escuro se o usuário tiver selecionado anteriormente
window.onload = () => {
    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }

    // Adicionar o evento para o botão de alternar
    const toggleButton = document.getElementById('toggle-dark-mode');
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleDarkMode);
    }
};
