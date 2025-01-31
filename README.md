# larm_thibault_lemoigne
Repository projet LARM

Ce projet contient les différents packages liés à l'UV LARM.

Vidéo : https://www.youtube.com/watch?v=wO5_Bc_lHiU&ab_channel=EmileThibault

Développé par :
- Emile Thibault
- Quentin Lemoigne

**Packages contenus :**
- tuto_move : Tutoriel lié au mouvements
- tuto_sim : Tutoriel lié à la simulation
- tuto_visio : Tutoriel lié à la vision
- grp_vincent : Lié aux challenges

# Informations de configuration

NETWORK_ID : 42

# Challenge 1 :

## Résumé

Ce package contient les nodes suivantes en plus de celles de base :
- scan_echo : Nettoie et transmet les données du laser sur un topic
- move : Gére le mouvement selon les informations du laser
- camera : Transmet les données de la camera sur un topic

## PC embarqué vincent :

Lancer Robot (Driver + Laser + Camera + Move):

```
ros2 launch grp_vincent tbot.launch.py
```


## PC controleur robnet :

```
ros2 launch grp_vincent visiualize.launch.py
```

## Simulation :

```
ros2 launch grp_vincent simulation.launch.py
```

# Commandes globales

## base only
```ros2 launch tbot_start base.launch.py```

## base + laser
```ros2 launch tbot_start minimal.launch.py```

## base + with laser + camera
```ros2 launch tbot_start full.launch.py```


## VOir le graphique des frame
```
ros2 run tf2_tools view_frames.py
```

## RVIZ2

```
rviz2
```
