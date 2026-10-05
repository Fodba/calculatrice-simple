## Brief: Calculatrice Simple

Ce package permet d'effectuer des calculs mathématiques avec les opérations de base et le calcul du reste d'une division.

Le script principal "main.py" appelle le module affichage. Ce module permet de demander 2 nombres ainsi que l'opération a effectuer et affiche son résultat.
Le programme s'execute et boucle tant que l'utilisateur n'a pas demander l'arrêt 

Chaque opération est gérée par son propre module.


## Fonctionnalités
- Choix de l'opération
- Addition
- Soustraction
- Multiplication
- Division
- Modulo


## Prérequis
Avant de commencer, assure-toi d'avoir installé :
* **Python 3.10** ou version supérieure.
* Le gestionnaire de paquets `pip`.


## Installation

**Créer et activer un environnement virtuel (Recommandé) :**
   
```bash
    python3 -m venv .venv
```

   # Sur Windows:
```bash
   .venv\Scripts\activate
```

Sur macOS/Linux:
```bash
   source .venv/bin/activate
```
   
**Installer les dépendances :**
   
```bash
   pip install -r requirements.txt
```
   
## Utilisation

Voici comment lancer le script principal :
```bash
    python3 main.py
```
Le script demande à l'utilisateur quelle opération il souhaite effectuer.
Il lui demande ensuite d'entrer les 2 nombres.
Il effectue le calcul et affiche le résultat.
Il demande si l'utilisateur veut faire un autre calcul ou quitter l'application.


## Codage
* **Clovis** - *Développeur*
* **Mauro** - *Développeur*
* **Xavier** - *Développeur*
