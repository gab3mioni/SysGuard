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
        return <p>Carregando...</p>;
    }

    return (
        <div>
            <h1>Métricas do Servidor</h1>
            <ul>
                {Object.entries(data).map(([key, value]) => (
                    <li key={key}>
                        {key}: {value}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;