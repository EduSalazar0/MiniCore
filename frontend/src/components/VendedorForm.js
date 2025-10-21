import React, { useState } from 'react';

function VendedorForm({ onVendedorAdded }) {
    const [nombre, setNombre] = useState('');
    const [totalFacturado, setTotalFacturado] = useState('');
    const [totalCobrado, setTotalCobrado] = useState('');
    const [porcentajeComision, setPorcentajeComision] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault(); // Evita que la página se recargue

        const vendedorData = {
            nombre,
            total_facturado: parseFloat(totalFacturado),
            total_cobrado: parseFloat(totalCobrado),
            porcentaje_comision: parseFloat(porcentajeComision)
        };

        onVendedorAdded(vendedorData); // Llama a la función del componente padre

        // Limpia los campos del formulario
        setNombre('');
        setTotalFacturado('');
        setTotalCobrado('');
        setPorcentajeComision('');
    };

    return (
        <form onSubmit={handleSubmit} className="vendedor-form">
            <h3>Agregar Nuevo Vendedor</h3>
            <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Nombre del vendedor" required />
            <input type="number" value={totalFacturado} onChange={(e) => setTotalFacturado(e.target.value)} placeholder="Total Facturado ($)" required />
            <input type="number" value={totalCobrado} onChange={(e) => setTotalCobrado(e.target.value)} placeholder="Total Cobrado ($)" required />
            <input type="number" value={porcentajeComision} onChange={(e) => setPorcentajeComision(e.target.value)} placeholder="Porcentaje de Comisión (%)" required />
            <button type="submit">Calcular y Guardar</button>
        </form>
    );
}

export default VendedorForm;