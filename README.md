## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Prérequis pour le déploiement:
- Un compte Github
- Un compte Circle/CI
- Un compte Heroku
- Un compte Sentry

 Le déploiement s'effectue via un pipeline CI/CD composé de plusieurs étapes.Le repository Git est lié a une organisation sur Circle/CI.
 Lorsqu'un changement est effectué sur la branche master du repository Git le pipeline est activé automatiquement, si le code passe les tests définis
 dans le workflow présent dans le fichier config.yml dans le dossier .circleci, une nouvelle image docker est crée et poussée sur DockerHub.
 Cette image est ensuite déployée sur une application Heroku a partir de laquelle elle est accessible.
 Si vous faites parti de l'organisation Circle/CI, vous pouvez redéployer l'application soit en relançant le dernier workflow réussi ou en créant un
 nouveau commit sur la branche master (les commit effectué sur les autres branches ne seront pas déployés).

  Si vous n'êtes pas membre de l'organisation vous pourez redéployer l'application en suivant la procédure décrite ci-dessous (a condition d'avoir tout 
  les éléments mentionnés dans la liste des prérequis):
- Créer un nouveau repository depuis votre compte GitHub en clonant le code présent ici:
```
https://github.com/ClemRoy/OrangeCountyLettings.git
```
- Connectez vous a votre compte Circle/CI et liez le au repository crée sur votre compte Github.
- Une fois cette étape effectuée, rendez vous dans l'onglet "project settings" correspondant au projet en question sur l'interface de Circle/CI et accedez 
a la page "Environment variables" a l'interieur de celui ci pour y ajouter la liste de variable suivante:
  - DOCKERHUB_PASSWORD: le mot de passe de votre compte Dockerhub
  - DOCKERHUB_USERNAME: votre nom d'utilisateur Dockerhub
  - HEROKU_API_KEY: la clé API lié a votre compte Heroku, trouvable dans votre "account settings" sur Heroku
  - HEROKU_EMAIL: l'email lié a votre compte heroku
  - SECRET_KEY: la clé secrete du projet django, si vous ne l'avez plus vous pouvez un régenerer une nouvelle a l'aide du guide ci dessous:
  ```
  https://codinggear.blog/django-generate-secret-key/#step-1-access-the-python-interactive-shell
  ```
  - SENTRY_ORG: le nom de votre organisation sur Sentry
  - SENTRY_PROJECT: le nom de votre project sur Sentry
  Vou pouvez trouver ces dernières en vous connectant a votre compte sentry et en accédant au projet que vous avez créer pour acceuillir les logs, elle seront présente dans l'url du site sous cette forme:
  ```
  https://SENTRY_ORG.sentry.io/projects/SENTRY_PROJECTs/?project=XXXXXX
  ```
  - SENTRY_AUTH_TOKEN: vous pouvez la créer en allant dans l'onglet settings de votre projet Sentry sous le nom de Security Token "Auth Tokens"

  Toutes ces variables d'environment sont indispensable pour pouvoir déployer le site via circle/CI.Veuillez noter que si l'une de ces variable comprend un carractère "$"
  vous devrez échapper le caractère un question en plaçant un "\" avant celui ci sinon la variable ne fonctionnerat pas correctement.

  Une fois ces informations remplies,rendez vous dans le fichier config.yml et remplacez toutes les instances de: 
  ```
  clementroy/orangecountylettings
  ```
  par 
  ```
  votre-nom-d'utilisateur-docker/orangecountylettings
  ```

  Enfin, rendez vous dans settings.py dans le dossier oc_lettings_site et remplacez la variable dsn a la ligne 136 par celle fournies dans l'onglet Client Keys(DSN)
  dans les settings de votre projet sur Sentry.

  Une fois toutes ces étapes accomplies,vous devriez pouvoir déployer l'application en effectuant un commit sur la branche master.