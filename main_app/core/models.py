import mongoengine as db
import datetime

class User(db.Document):
    email = db.EmailField(verbose_name='email')
    phone = db.StringField(max_length=12)
    username = db.StringField(verbose_name='username')
    is_active = db.BooleanField(default=False)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow())

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "is_active": self.is_active,
            "created_at": self.created_at
        }


class Messages(db.Document):
    id = db.IntField()
    sender = db.ReferenceField(User)
    receiver = db.ReferenceField(User)
    message = db.StringField(max_length=255)
    is_read = db.BooleanField(required=False, default=False)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow())

    def to_json(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message,
            "created_at": self.created_at
        }


user = User(email="test@gmail.com", phone="99522735099",
            username="test123", created_at="01/01/2022")
# user.save()
# user1 = User(email="test1@gmail.com", phone="99522735099",
#              username="test1232", created_at="01/01/2022")
# user1.save()

# message = Messages(sender=user, receiver=user1,
#                    message="hello, test", created_at="01/01/2022")

# message.save()
print(user.email)
