import React, { useState } from 'react';
import { calcularComision } from './services/vendedorService';
import './App.css';

function App() {
    const [vendedorNombre, setVendedorNombre] = useState('Ana'); // Valor por defecto
    const [fechaInicio, setFechaInicio] = useState('');
    const [fechaFin, setFechaFin] = useState('');
    const [resultado, setResultado] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setResultado(null);
        setLoading(true);

        const requestData = {
            vendedor_nombre: vendedorNombre,
            fecha_inicio: fechaInicio,
            fecha_fin: fechaFin,
        };

        try {
            const data = await calcularComision(requestData);
            setResultado(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Calculadora de Comisiones</h1>
            </header>
            <main>
                <form onSubmit={handleSubmit} className="vendedor-form">
                    <select value={vendedorNombre} onChange={(e) => setVendedorNombre(e.target.value)}>
                        <option value="Ana">Ana</option>
                        <option value="Juan">Juan</option>
                        <option value="Maria">Maria</option>
                        <option value="Pedro">Pedro</option>
                    </select>
                    <input type="date" value={fechaInicio} onChange={(e) => setFechaInicio(e.target.value)} required />
                    <input type="date" value={fechaFin} onChange={(e) => setFechaFin(e.target.value)} required />
                    <button type="submit" disabled={loading}>
                        {loading ? 'Calculando...' : 'Calcular Comisión'}
                    </button>
                </form>

                {error && <p className="error-message">Error: {error}</p>}

                {resultado && (
                    <div className="resultado-card">
                        <h3>Resultados para {vendedorNombre}</h3>
                        <div className="resultado-item">
                            <span>Total en Ventas:</span>
                            <strong>${resultado.total_ventas.toFixed(2)}</strong>
                        </div>
                        <div className="resultado-item">
                            <span>Porcentaje de Comisión:</span>
                            <strong>{resultado.porcentaje_comision}%</strong>
                        </div>
                        <div className="resultado-item-total">
                            <span>Monto de Comisión:</span>
                            <strong>${resultado.monto_comision.toFixed(2)}</strong>
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
}

export default App;