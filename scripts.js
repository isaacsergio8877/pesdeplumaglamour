function abrirModal(titulo, descricao, preco) {
    document.getElementById('modal-title').innerText = titulo;
    document.getElementById('modal-description').innerText = descricao;
    document.getElementById('modal-price').innerText = preco;
    document.getElementById('modal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function fecharModal() {
    document.getElementById('modal').style.display = 'none';
    document.body.style.overflow = 'auto';
}
