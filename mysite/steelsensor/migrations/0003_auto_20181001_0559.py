# Generated by Django 2.1.1 on 2018-10-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steelsensor', '0002_storedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='fingerprint',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='hash',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='path',
            field=models.TextField(),
        ),
    ]
