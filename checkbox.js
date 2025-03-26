document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
  checkbox.addEventListener('change', () => {
    checkbox.checked ? console.log('Checked') : console.log('Not checked');
  });
}
