from db.connectionDB import ConnectionDB
from persistence.models import AuthUser
from sqlalchemy.orm import Session

class AuthUserRp(ConnectionDB):
        
    def getUserByName(self, user_name:str):
        user : AuthUser = None
        with Session(self.engine) as session:
            user = session.query(AuthUser).filter_by(userBD = user_name).first()
        return user
    
    def insertUser(self, user:AuthUser):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()