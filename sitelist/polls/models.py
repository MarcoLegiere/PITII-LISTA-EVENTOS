from django.db import models
class User(models.Model):
    __tablename__ = "users"

    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=120)

    def __init__(self, password, email):
        self.password = password
        self.email = email


    def __repr__(self):
        return "<User %r>" % self.email


class meeting(models.Model):
    __tablename__ = "meeting"

    id = models.IntegerField(primary_key=True)
    name_meeting = models.CharField(max_length=120)
    author = models.CharField(max_length=80)
    date_meeting = models.DateField()

    def __init__(self, name_meeting, author, date_meeting, user_id):
        self.name = name_meeting
        self.author = author
        self.date_meeting = date_meeting
        self.user_id = user_id

    def __repr__(self):
        return "Meeting %r>" % self.id


class Confirm(models.Model):
    __tablename__ = "confirm"

    id = models.IntegerField(primary_key=True)
    name_meeting = models.CharField(max_length=120)
    matricula = models.CharField(max_length=10)
    email = models.CharField(max_length=120)
    setor = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __int__(self, name_meeting, matricula, email, setor, cargo):
        self.name_meeting = name_meeting
        self.matricula = matricula
        self.email = email
        self.setor = setor
        self.cargo = cargo

    def __repr__(self):
        return "<Confirm %r>" % self.id
