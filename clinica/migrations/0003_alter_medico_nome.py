# Generated by Django 4.2 on 2025-04-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_rename_espe_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='nome',
            field=models.CharField(blank=True, default='dori', max_length=10),
            preserve_default=False,
        ),
    ]
