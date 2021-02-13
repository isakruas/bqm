# Generated by Django 3.0.7 on 2021-01-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superior', models.IntegerField()),
                ('inferior', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Filiação',
                'verbose_name_plural': 'Filiações',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(blank=None, max_length=30)),
                ('sobrenome', models.CharField(blank=None, max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('escolaridade', models.CharField(blank=None, max_length=255, verbose_name='Escolaridade')),
                ('nivel_de_acesso', models.CharField(blank=None, default='epsilon', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['id'],
            },
        ),
    ]
