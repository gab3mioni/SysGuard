import React, { useState } from 'react';
import DataFetcher from './components/DataFetcher/DataFetcher';
import PowerBIChart from './components/PowerBIChart/PowerBIChart';

function App() {
    const [data, setData] = useState({});

    const handleDataFetched = (fetchedData) => {
        setData(fetchedData);
    };

    return (
        <div className="container my-5">
            <h1 className="text-center mb-4">Métricas do Servidor</h1>

            {/* Componente DataFetcher que atualiza os dados */}
            <DataFetcher onDataFetched={handleDataFetched}/>

            {/* Exibição dos dados */}
            {Object.keys(data).length === 0 ? (
                <p>Sem dados para exibir. Aguarde...</p>
            ) : (
                <ul className="list-group">
                    {Object.entries(data).map(([key, value]) => (
                        <li key={key} className="list-group-item d-flex justify-content-between align-items-center">
                            <strong>{key}</strong>
                            <span>{value}</span>
                        </li>
                    ))}
                </ul>
            )}

            {/* Componente PowerBIChart */}
            <div
                style={{
                    height: '100%',
                    width: '100%',
                    backgroundColor: '#f8f9fa',
                    padding: '1rem',
                    borderRadius: '8px',
                }}
                className="my-3"
            >
                <PowerBIChart/>
            </div>
        </div>
    );
}

export default App;
