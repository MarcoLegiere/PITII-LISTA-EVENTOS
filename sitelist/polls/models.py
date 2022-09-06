import uuid
from django.contrib.auth.models import User
from datetime import date

from django.db import models

class Meeting(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID UNICO')
    name_meeting = models.CharField(max_length=120, verbose_name='Nome da reunião')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Autor')
    date_meeting = models.DateField(verbose_name='Data da reunião')
    link = models.CharField(max_length=400, blank=True, verbose_name='Link da reunião')
    #borrower = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name='Autor', blank=False)

    MEETING_PUBLIC = (
        ('p', 'Publicado'),
        ('a', 'Arquivado')
    )

    public = models.CharField(
        max_length=1,
        choices=MEETING_PUBLIC,
        blank=False,
        default='p',
        help_text='Publicar ou Arquivar',
    )

    MEETING_LOCAL = (
        ('p', 'Presencial'),
        ('o', 'Online')
    )

    local = models.CharField(
        max_length=1,
        choices=MEETING_LOCAL,
        blank=False,
        default='p',
        help_text='Local Reunião',
    )

    MEETING_STATUS = (
        ('p', 'Público'),
        ('f', 'Fechado')
    )

    status = models.CharField(
        max_length=1,
        choices=MEETING_STATUS,
        blank=False,
        default='f',
        help_text='Status da reunião',
    )


    def __int__(self, name_meeting, author, date_meeting, link):

        self.name = name_meeting
        self.author = author
        self.date_meeting = date_meeting
        self.link = link

    def __str__(self):
        return f'HRJ - {self.name_meeting}'

    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

class Owner(models.Model):

    name = models.CharField(max_length=80, verbose_name='Nome')
    password = models.CharField(max_length=50, verbose_name='Senha')
    email = models.CharField(max_length=120, verbose_name='E-mail')

    class Meta:
        ordering = ['name', 'email']

    def __int__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __str__(self):
        return self.name



class User(models.Model):

    name = models.CharField(max_length=80)
    matricula = models.CharField(max_length=10)
    email = models.CharField(max_length=120)
    setor = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, verbose_name='Nome da Reunião')

    def __int__(self, name, name_meeting, matricula, email, setor, cargo):
        self.name = name
        self.name_meeting = name_meeting
        self.matricula = matricula
        self.email = email
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return self.name
