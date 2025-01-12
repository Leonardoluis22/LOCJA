function openDeleteModal(deleteUrl) {
    const modal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');

    modal.classList.remove('hidden');
    deleteForm.action = deleteUrl;
}

function closeDeleteModal() {
    const modal = document.getElementById('deleteModal');
    modal.classList.add('hidden');
}

// Fechar modal ao clicar fora dele
document.addEventListener('click', function (event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        closeDeleteModal();
    }
});

