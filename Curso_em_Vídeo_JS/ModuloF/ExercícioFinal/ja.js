document.addEventListener('DOMContentLoaded', () => {
    let vetor = [];

    const numeroInput = document.getElementById('numeroInput');
    const adicionarBtn = document.getElementById('adicionarBtn');
    const numeroList = document.getElementById('numeroList');
    const finalizarBtn = document.getElementById('finalizarBtn');

    adicionarBtn.addEventListener('click', () => {
        const numero = parseInt(numeroInput.value);

        if (!isNaN(numero) && numero >= 1 && numero <= 100 && !vetor.includes(numero)) {
            vetor.push(numero);
            const option = document.createElement('option');
            option.textContent = `Valor ${numero} adicionado.`;
            numeroList.appendChild(option);
            numeroInput.value = '';
            numeroInput.focus();
        } else {
            alert('Por favor, digite um número válido entre 1 e 100 que não foi adicionado antes.');
        }
    });

    finalizarBtn.addEventListener('click', () => {
        if (vetor.length === 0) {
            alert('Adicione números antes de finalizar.');
        } else {
            alert(`Números adicionados: ${vetor.join(', ')}`);
        }
    });
});
