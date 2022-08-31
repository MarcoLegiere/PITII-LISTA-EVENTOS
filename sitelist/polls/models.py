import uuid

from django.db import models

class Meeting(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID UNICO')
    name_meeting = models.CharField(max_length=120, verbose_name='Nome da reunião')
    author = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name='Autor', blank=False)
    date_meeting = models.DateField(verbose_name='Data da reunião')


    MEETING_STATUS = (
        ('p', 'Presencial'),
        ('o', 'Online')
    )

    status = models.CharField(
        max_length=1,
        choices=MEETING_STATUS,
        blank=False,
        default='p',
        help_text='Local Reunião',
    )

    def __int__(self, name_meeting, author, date_meeting):

        self.name = name_meeting
        self.author = author
        self.date_meeting = date_meeting

    def __str__(self):
        return f'HRJ - {self.name_meeting}'

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
