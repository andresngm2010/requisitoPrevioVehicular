document.addEventListener("DOMContentLoaded", function() {
    const provinciaSelect = document.getElementById('id_provincia');
    const cantonSelect = document.getElementById('id_canton');
    const agenciaSelect = document.getElementById('id_agencia');

    provinciaSelect.addEventListener('change', function() {
        const provinciaId = provinciaSelect.value;
        if (provinciaId) {
            fetch(`/cargar-cantones/?provincia_id=${provinciaId}`)
                .then(response => response.json())
                .then(data => {
                    cantonSelect.innerHTML = '<option value="">Seleccione un cantón</option>';
                    agenciaSelect.innerHTML = '<option value="">Seleccione una agencia</option>';
                    data.forEach(canton => {
                        const option = document.createElement('option');
                        option.value = canton.id;
                        option.textContent = canton.nombre;
                        cantonSelect.appendChild(option);
                    });
                });
        } else {
            cantonSelect.innerHTML = '<option value="">Seleccione un cantón</option>';
            agenciaSelect.innerHTML = '<option value="">Seleccione una agencia</option>';
        }
    });

    cantonSelect.addEventListener('change', function() {
        const cantonId = cantonSelect.value;
        if (cantonId) {
            fetch(`/cargar-agencias/?canton_id=${cantonId}`)
                .then(response => response.json())
                .then(data => {
                    agenciaSelect.innerHTML = '<option value="">Seleccione una agencia</option>';
                    data.forEach(agencia => {
                        const option = document.createElement('option');
                        option.value = agencia.id;
                        option.textContent = agencia.nombre;
                        agenciaSelect.appendChild(option);
                    });
                });
        } else {
            agenciaSelect.innerHTML = '<option value="">Seleccione una agencia</option>';
        }
    });
});
