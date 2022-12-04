# Generated by Django 4.1.3 on 2022-12-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Valorant', '0002_alter_duo_player_rank_alter_player_player_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duo',
            name='player_rank',
            field=models.CharField(choices=[('IRON1', 'IRON I'), ('IRON2', 'IRON II'), ('IRON3', 'IRON III'), ('BRONZE1', 'BRONZE I'), ('BRONZE2', 'BRONZE II'), ('BRONZE3', 'BRONZE III'), ('SILVER1', 'SILVER I'), ('SILVER2', 'SILVER II'), ('SILVER3', 'SILVER III'), ('GOLD1', 'GOLD I'), ('GOLD2', 'GOLD II'), ('GOLD3', 'GOLD III'), ('PLATINUM1', 'PLATINUM I'), ('PLATINUM2', 'PLATINUM II'), ('PLATINUM3', 'PLATINUM III'), ('DIAMOND1', 'DIAMOND I'), ('DIAMOND2', 'DIAMOND II'), ('DIAMOND3', 'DIAMOND III'), ('ASCENDANT1', 'ASCENDANT I'), ('ASCENDANT2', 'ASCENDANT II'), ('ASCENDANT3', 'ASCENDANT III'), ('IMMORTAL1', 'IMMORTAL I'), ('IMMORTAL2', 'IMMORTAL II'), ('IMMORTAL3', 'IMMORTAL III'), ('RADIANT', 'RADIANT')], default='Unspecified', max_length=30),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_rank',
            field=models.CharField(choices=[('IRON1', 'IRON I'), ('IRON2', 'IRON II'), ('IRON3', 'IRON III'), ('BRONZE1', 'BRONZE I'), ('BRONZE2', 'BRONZE II'), ('BRONZE3', 'BRONZE III'), ('SILVER1', 'SILVER I'), ('SILVER2', 'SILVER II'), ('SILVER3', 'SILVER III'), ('GOLD1', 'GOLD I'), ('GOLD2', 'GOLD II'), ('GOLD3', 'GOLD III'), ('PLATINUM1', 'PLATINUM I'), ('PLATINUM2', 'PLATINUM II'), ('PLATINUM3', 'PLATINUM III'), ('DIAMOND1', 'DIAMOND I'), ('DIAMOND2', 'DIAMOND II'), ('DIAMOND3', 'DIAMOND III'), ('ASCENDANT1', 'ASCENDANT I'), ('ASCENDANT2', 'ASCENDANT II'), ('ASCENDANT3', 'ASCENDANT III'), ('IMMORTAL1', 'IMMORTAL I'), ('IMMORTAL2', 'IMMORTAL II'), ('IMMORTAL3', 'IMMORTAL III'), ('RADIANT', 'RADIANT')], default='Unspecified', max_length=30),
        ),
    ]
