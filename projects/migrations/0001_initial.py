

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(max_length=70)),
                ('situacao', models.CharField(max_length=50)),
            ],
        ),
    ]
