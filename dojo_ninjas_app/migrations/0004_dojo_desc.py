# Generated by Django 2.2 on 2020-03-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_remove_ninja_dojo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='old dojo', max_length=45),
            preserve_default=False,
        ),
    ]
