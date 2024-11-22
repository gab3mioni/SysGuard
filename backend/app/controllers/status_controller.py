from flask import jsonify

class StatusController:
    @staticmethod
    def get_status():
        """
        Endpoint para verificar o status do backend.

        Retorna:
            json: Um objeto JSON com a mensagem indicando que o backend está online.
            Exemplo de resposta:
            {
                "status": "Back online!"
            }
        """
        return jsonify({"status": "Back online!"})