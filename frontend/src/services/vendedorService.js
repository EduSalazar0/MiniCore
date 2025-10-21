const API_URL = 'http://127.0.0.1:8000';

export const calcularComision = async (calculadoraData) => {
    const response = await fetch(`${API_URL}/calculadora/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(calculadoraData),
    });
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error al calcular la comisión');
    }
    return await response.json();
};