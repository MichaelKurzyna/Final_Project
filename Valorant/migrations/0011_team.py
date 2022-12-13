# Generated by Django 4.1.3 on 2022-12-13 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Valorant', '0010_duo_user_name_player_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('player_name', models.CharField(max_length=30)),
                ('player_rank', models.CharField(choices=[('IRON I', 'IRON1'), ('IRON II', 'IRON2'), ('IRON III', 'IRON3'), ('BRONZE I', 'BRONZE1'), ('BRONZE II', 'BRONZE2'), ('BRONZE III', 'BRONZE3'), ('SILVER I', 'SILVER1'), ('SILVER II', 'SILVER2'), ('SILVER III', 'SILVER3'), ('GOLD I', 'GOLD1'), ('GOLD II', 'GOLD2'), ('GOLD III', 'GOLD3'), ('PLATINUM I', 'PLATINUM1'), ('PLATINUM II', 'PLATINUM2'), ('PLATINUM III', 'PLATINUM3'), ('DIAMOND I', 'DIAMOND1'), ('DIAMOND II', 'DIAMOND2'), ('DIAMOND III', 'DIAMOND3'), ('ASCENDANT I', 'ASCENDANT1'), ('ASCENDANT II', 'ASCENDANT2'), ('ASCENDANT III', 'ASCENDANT3'), ('IMMORTAL I', 'IMMORTAL1'), ('IMMORTAL II', 'IMMORTAL2'), ('IMMORTAL III', 'IMMORTAL3'), ('RADIANT', 'RADIANT')], default='Unspecified', max_length=30)),
                ('players_signedup', models.CharField(blank=True, max_length=1000)),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]