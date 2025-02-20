from typing import Callable
from loguru import logger
from rest_framework import status
from rest_framework.response import Response


def exception_handler(exc_place: str):
    """
    Хэндлер для отслеживания и логирования неожиданных ошибок в методах

    :param exc_place: Местонахождение метода
    :return: Response
    """
    def inner_decorator(func: Callable):
        def wrapped(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{exc_place}: {e}")
                response = Response({'error': f'{e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return response
        return wrapped
    return inner_decorator