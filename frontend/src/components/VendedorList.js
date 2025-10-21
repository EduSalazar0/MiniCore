import React from 'react';

function VendedorList({ vendedores }) {
    return (
        <div className="vendedor-list">
            <h3>Registro de Comisiones</h3>
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Total Facturado</th>
                        <th>Total Cobrado</th>
                        <th>Comisión (%)</th>
                        <th>Monto Comisión</th>
                        <th>Pago Realizado</th>
                    </tr>
                </thead>
                <tbody>
                    {vendedores.map(v => (
                        <tr key={v.id}>
                            <td>{v.nombre}</td>
                            <td>${v.total_facturado.toFixed(2)}</td>
                            <td>${v.total_cobrado.toFixed(2)}</td>
                            <td>{v.porcentaje_comision}%</td>
                            <td><b>${v.comision_calculada.toFixed(2)}</b></td>
                            <td className={v.pago_realizado ? 'pago-si' : 'pago-no'}>
                                {v.pago_realizado ? 'Sí ✅' : 'No ❌'}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default VendedorList;