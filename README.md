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

## Déploiement

### Prérequis:

1. Un compte GitHub
2. Un compte CircleCI
3. Un compte Heroku
4. Un compte Sentry

### Pipeline CI/CD

  Le déploiement de l'application se fait à travers un pipeline CI/CD composé de plusieurs étapes. Le repository Git est lié à une organisation sur CircleCI. Lorsqu'un changement est effectué sur la branche master, le pipeline est automatiquement déclenché. Si le code réussit les tests définis dans le fichier config.yml du dossier .circleci, une nouvelle image Docker est créée et poussée sur DockerHub. Cette image est ensuite déployée sur une application Heroku.

### Procédure de déploiement

  Si vous faites partie de l'organisation CircleCI, vous pouvez redéployer l'application en relançant le dernier workflow réussi ou en créant un nouveau commit sur la branche master. Notez que seuls les commits effectués sur la branche master seront déployés.

  Si vous n'êtes pas membre de l'organisation, suivez les étapes ci-dessous pour déployer l'application :

  1. Créez un nouveau repository depuis votre compte GitHub en clonant le code présent ici :
  ```
  https://github.com/ClemRoy/OrangeCountyLettings.git
  ```
  2. Connectez-vous à votre compte CircleCI et liez-le au repository créé sur votre compte GitHub.

  3. Accédez à l'onglet "Project Settings" correspondant au projet sur l'interface de CircleCI, puis rendez-vous dans la section "Environment Variables". Ajoutez les variables d'environnement suivantes :

  - DOCKERHUB_PASSWORD : le mot de passe de votre compte DockerHub
  - DOCKERHUB_USERNAME : votre nom d'utilisateur DockerHub
  - HEROKU_API_KEY : la clé API associée à votre compte Heroku (trouvable dans les paramètres de votre compte Heroku)
  - HEROKU_EMAIL : l'adresse e-mail associée à votre compte Heroku
  - SECRET_KEY : la clé secrète du projet Django. Si vous ne l'avez plus, vous pouvez en générer une nouvelle à l'aide du guide suivant :
    ```
    https://codinggear.blog/django-generate-secret-key/#step-1-access-the-python-interactive-shell
    ```
  - SENTRY_ORG : le nom de votre organisation sur Sentry
  -  SENTRY_PROJECT : le nom de votre projet sur Sentry. Vous pouvez trouver ces informations en vous connectant à votre compte Sentry et en accédant au projet que vous avez créé pour accueillir les logs. Les informations seront présentes dans l'URL du site sous cette forme :
    ```
    https://SENTRY_ORG.sentry.io/projects/SENTRY_PROJECTs/?project=XXXXXX
    ```
  - SENTRY_AUTH_TOKEN : vous pouvez la créer en allant dans l'onglet "Settings" de votre projet Sentry sous le nom de "Security Token" -> "Auth Tokens"

  Il est important de noter que si l'une de ces variables contient un caractère $, vous devez échapper le caractère en plaçant un \ devant, sinon la variable ne fonctionnera pas correctement.

  4. Une fois ces informations renseignées, rendez-vous dans le fichier config.yml et remplacez toutes les occurrences de :
    ```
    clementroy/orangecountylettings
    ```
  par 
    ```
    votre-nom-d'utilisateur-docker/orangecountylettings
    ```

  5. Enfin, ouvrez le fichier settings.py dans le dossier oc_lettings_site et remplacez la valeur de la variable DSN à la ligne 136 par celle fournie dans l'onglet "Client Keys (DSN)" des paramètres de votre projet sur Sentry.

  Une fois ces étapes terminées, vous pouvez déployer l'application en effectuant un commit sur la branche master. Seuls les commits sur cette branche déclencheront le déploiement.