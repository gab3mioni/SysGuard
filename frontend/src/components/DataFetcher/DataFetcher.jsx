import React, { useEffect, useState, useCallback } from "react";
import api from '../../services/api';

const DataFetcher = ({ onDataFetched }) => {
    const [loading, setLoading] = useState(true);

    const fetchData = useCallback(async () => {
        try {
            const response = await api.get('/metrics');
            console.log('Dados recebidos:', response.data);
            onDataFetched(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Erro ao consumir a API: ', error);
            setLoading(false);
        }
    }, [onDataFetched]);

    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 5000);
        return () => clearInterval(interval);
    }, [fetchData]);

    if (loading) {
        return (
            <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
                <p>Carregando...</p>
            </div>
        );
    }

    return null;
};

export default DataFetcher;
