import uuid
from django.contrib.auth.models import User
from django.db import models


class Meeting(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name_meeting = models.CharField(max_length=120, unique=True, verbose_name='Nome da reunião')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_meeting = models.DateField(verbose_name='Data da reunião')
    link = models.CharField(max_length=400, blank=True, verbose_name='Link da reunião')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

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

    def __int__(self, name_meeting, author, date_meeting, link, descricao):
        self.name = name_meeting
        self.author = author
        self.date_meeting = date_meeting
        self.link = link
        self.descricao = descricao

    def __str__(self):
        return self.name_meeting


class Owner(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nome')
    password = models.CharField(max_length=50, verbose_name='Senha')
    email = models.EmailField(max_length=120, verbose_name='E-mail')

    class Meta:
        ordering = ['name', 'email']

    def __int__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __str__(self):
        return self.name