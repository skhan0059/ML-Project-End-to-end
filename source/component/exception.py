import sys
from typing import Tuple


def error_message_detail(error: Exception, error_details: sys) -> str:
    """
    Extract file name and line number from the traceback to enrich the error.
    """
    _, _, exc_tb = error_details.exc_info()  # type: Tuple[type, BaseException, object]
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    line_no = exc_tb.tb_lineno if exc_tb else "Unknown"
    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"line number [{line_no}] error message [{error}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message