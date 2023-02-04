from fastapi import HTTPException


class UserNotFound(HTTPException):
    pass


class IncorrectPassword(HTTPException):
    pass


class URLNotValid(HTTPException):
    pass


class URLIntegrityError(HTTPException):
    pass


class AdminNotFound(HTTPException):
    pass


class URLForwardError(HTTPException):
    pass