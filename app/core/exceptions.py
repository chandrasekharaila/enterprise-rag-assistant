from fastapi import Request
from fastapi.responses import JSONResponse


class EnterpriseRAGException(Exception):

    def __init__(self, message: str):
        self.message = message


async def enterprise_exception_handler(
    request: Request,
    exc: EnterpriseRAGException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message
        }
    )