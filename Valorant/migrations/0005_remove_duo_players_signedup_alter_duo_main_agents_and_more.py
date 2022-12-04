# Generated by Django 4.1.3 on 2022-12-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Valorant', '0004_alter_duo_main_agents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duo',
            name='players_signedup',
        ),
        migrations.AlterField(
            model_name='duo',
            name='main_agents',
            field=models.CharField(choices=[('No main', 'NONE'), ('Brimstone', 'Brimstone'), ('Pheonix', 'Pheonix'), ('Sage', 'Sage'), ('Sova', 'Sova'), ('Viper', 'Viper'), ('Cypher', 'Cypher'), ('Reyna', 'Reyna'), ('Killjoy', 'Killjoy'), ('Breach', 'Breach'), ('Omen', 'Omen'), ('Jett', 'Jett'), ('Raze', 'Raze'), ('Skye', 'Skye'), ('Yoru', 'Yoru'), ('Astra', 'Astra'), ('Kayo', 'Kayo'), ('Chamber', 'Chamber'), ('Neon', 'Neon'), ('Fade', 'Fade'), ('Harbor', 'Harbor')], default='NONE', max_length=300),
        ),
        migrations.AlterField(
            model_name='duo',
            name='player_rank',
            field=models.CharField(choices=[('IRON I', 'IRON1'), ('IRON II', 'IRON2'), ('IRON III', 'IRON3'), ('BRONZE I', 'BRONZE1'), ('BRONZE II', 'BRONZE2'), ('BRONZE III', 'BRONZE3'), ('SILVER I', 'SILVER1'), ('SILVER II', 'SILVER2'), ('SILVER III', 'SILVER3'), ('GOLD I', 'GOLD1'), ('GOLD II', 'GOLD2'), ('GOLD III', 'GOLD3'), ('PLATINUM I', 'PLATINUM1'), ('PLATINUM II', 'PLATINUM2'), ('PLATINUM III', 'PLATINUM3'), ('DIAMOND I', 'DIAMOND1'), ('DIAMOND II', 'DIAMOND2'), ('DIAMOND III', 'DIAMOND3'), ('ASCENDANT I', 'ASCENDANT1'), ('ASCENDANT II', 'ASCENDANT2'), ('ASCENDANT III', 'ASCENDANT3'), ('IMMORTAL I', 'IMMORTAL1'), ('IMMORTAL II', 'IMMORTAL2'), ('IMMORTAL III', 'IMMORTAL3'), ('RADIANT', 'RADIANT')], default='Unspecified', max_length=30),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_rank',
            field=models.CharField(choices=[('IRON I', 'IRON1'), ('IRON II', 'IRON2'), ('IRON III', 'IRON3'), ('BRONZE I', 'BRONZE1'), ('BRONZE II', 'BRONZE2'), ('BRONZE III', 'BRONZE3'), ('SILVER I', 'SILVER1'), ('SILVER II', 'SILVER2'), ('SILVER III', 'SILVER3'), ('GOLD I', 'GOLD1'), ('GOLD II', 'GOLD2'), ('GOLD III', 'GOLD3'), ('PLATINUM I', 'PLATINUM1'), ('PLATINUM II', 'PLATINUM2'), ('PLATINUM III', 'PLATINUM3'), ('DIAMOND I', 'DIAMOND1'), ('DIAMOND II', 'DIAMOND2'), ('DIAMOND III', 'DIAMOND3'), ('ASCENDANT I', 'ASCENDANT1'), ('ASCENDANT II', 'ASCENDANT2'), ('ASCENDANT III', 'ASCENDANT3'), ('IMMORTAL I', 'IMMORTAL1'), ('IMMORTAL II', 'IMMORTAL2'), ('IMMORTAL III', 'IMMORTAL3'), ('RADIANT', 'RADIANT')], default='Unspecified', max_length=30),
        ),
    ]
