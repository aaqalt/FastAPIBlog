from passlib.context import CryptContext

pswd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    @staticmethod
    def bcrypt(password: str):
        return pswd_context.hash(password)

    @staticmethod
    def verify(hashed_password: str,password: str):
        return pswd_context.verify(password, hashed_password)
