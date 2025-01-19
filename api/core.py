from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import Header


class ResponseManager:
    "Core-класс для создания метода генерации ответа от сервера для reg_auth роутера"
    @staticmethod
    def generate_response(success, detail, headers: Optional[Header]):
        return JSONResponse(content={'success': success, 'detail': detail},
                            headers=headers)
