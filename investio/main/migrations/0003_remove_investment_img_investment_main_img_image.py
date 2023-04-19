# Generated by Django 4.2 on 2023-04-18 17:20

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_investment_img_alter_investment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='img',
        ),
        migrations.AddField(
            model_name='investment',
            name='main_img',
            field=models.FileField(blank=True, null=True, upload_to=main.models.make_file_path_1),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to=main.models.make_file_path_2)),
                ('investment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.investment')),
            ],
        ),
    ]