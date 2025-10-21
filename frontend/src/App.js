import React, { useState, useEffect } from 'react';
import VendedorForm from './components/VendedorForm';
import VendedorList from './components/VendedorList';
import { getVendedores, createVendedor } from './services/vendedorService';
import './App.css'; // Importaremos los estilos

function App() {
    const [vendedores, setVendedores] = useState([]); // Estado para guardar la lista de vendedores

    // useEffect se ejecuta cuando el componente se monta por primera vez
    useEffect(() => {
        loadVendedores();
    }, []);

    const loadVendedores = async () => {
        try {
            const data = await getVendedores();
            setVendedores(data);
        } catch (error) {
            console.error(error.message);
        }
    };

    const handleAddVendedor = async (vendedorData) => {
        try {
            const nuevoVendedor = await createVendedor(vendedorData);
            // Agrega el nuevo vendedor a la lista existente sin recargar la página
            setVendedores([...vendedores, nuevoVendedor]);
        } catch (error) {
            console.error(error.message);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Mini Core de Comisiones</h1>
            </header>
            <main>
                <VendedorForm onVendedorAdded={handleAddVendedor} />
                <VendedorList vendedores={vendedores} />
            </main>
        </div>
    );
}

export default App;