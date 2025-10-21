const API_URL = 'http://127.0.0.1:8000'; // La URL base del backend

export const getVendedores = async () => {
    const response = await fetch(`${API_URL}/vendedores/`);
    if (!response.ok) {
        throw new Error('Error al obtener los vendedores');
    }
    return await response.json();
};

export const createVendedor = async (vendedorData) => {
    const response = await fetch(`${API_URL}/vendedores/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(vendedorData),
    });
    if (!response.ok) {
        throw new Error('Error al crear el vendedor');
    }
    return await response.json();
};