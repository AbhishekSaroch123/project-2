# Generated by Django 4.2.5 on 2023-09-25 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0003_alter_education_user_alter_interests_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.user'),
        ),
        migrations.AlterField(
            model_name='interests',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.user'),
        ),
        migrations.AlterField(
            model_name='peoplealsoviewed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.user'),
        ),
        migrations.AlterField(
            model_name='peopleyoumayknow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.user'),
        ),
    ]
