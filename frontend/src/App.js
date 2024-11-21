import React, { useEffect, useState } from "react";
import api from './services/api';

function App() {
    const[data, setData] = useState({});
    const[loading, setLoading] = useState(true);

    const fetchData = async () => {
        try {
            const response = await api.get('/metrics');
            console.log('Dados recebidos:', response.data);
            setData(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Erro ao consumir a API: ', error);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 5000);
        return() => clearInterval(interval);
    }, []);

    if (loading) {
        return (
            <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
                <p>Carregando...</p>
            </div>
        );
    }

    return (
        <div className="container my-5">
            <h1 className="text-center mb-4">Métricas do Servidor</h1>
            <ul className="list-group">
                {Object.entries(data).map(([key, value]) => (
                    <li key={key} className="list-group-item d-flex justify-content-between align-items-center">
                        <strong>{key}</strong>
                        <span>{value}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;