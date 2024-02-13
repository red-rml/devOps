# DevOps  <a name="readme-top"></a>

## Auteurs 🎭

* **Bachekou DIABY** _alias_ [@Bachekou-DIABY](https://github.com/Bachekou-DIABY)
* **Rédouane RÉMILI** _alias_ [@FinOrfy](https://github.com/red-rml)

## Techno

* Docker
* Python
* Nginx
* MySQL
* Newman

---

### Mise en place Etape 1 : Infra standard via Docker

* BDD MySQL qui run dans un conteneur docker
* Back python
* Serveur Nginx
* Faire communiquer les services dans docker en les mettant tous dans le même network

### Difficulté/Solution : Etape 1

* Faire communiquer les différents containers comme le back-end python et la bdd MySQL :
  * Dans le fichier run.sh créer le network (sous-réseau) avec une IP fixe, avec à l’intérieur les différents services afin de permettre la communication entre ces services.

### Difficulté/Solution : Etape 2

* Installer Ansible : "Chemin source:/Chemin d’installation"
  * Option ```-v``` et enter le chemin source **absolu** 
* Faire fonctionner la simple commandes ```ansible -v``` :
  * Il faut installer ansible directement dans le container ou il y a tout le projet avec la commande : ```apt-get install ansible``` => Ensuite la commande  fonctionne.
* Veille version d'ubuntu et d'ansible qui provoquait des erreur car pas le module community.docker.docker_image
  * installation d'une version plus recente d'ubuntu
* Lorqu'on lance notre container ubuntu il s'arrête automatiquement.
  * Ne pas oublier le ```-i``` pour que le container tourne en continu avec la commande ```docker run --name ansible -v "cheminSource:/cheminDestination" -i  ansible```

### Ce qu’on retient 👍

* Créer un subnet pour faire communiquer les différents service dans docker
* Mise en place d'une infrastructure de base avec nginx, une bdd et un backend quelconque (ici python)
* Utilisation d'ansible pour realiser de la configuration automatisée
  
---

### Améliorations possible : sécurisé l'environnement

* Supprimer les fichiers .sql qui génerent la bdd et un utilisateur. Créer plutôt des variables d'environnement sur Github pour ne pas avoir à pousser ces fichiers dans le ripot.
* Configurer nginx qui est le point d'entrer back end pour le sécuriser : setup le Https (mettre en place les certificats).
* Rediriger toutes les requettes émisent au serveur python vers le serveur nginx qui sera configurer en https
* S'assurer que les versions des packages soit toujours maintenus, sécurisés et compatible.
* Enfin protéger le ripot github en protégeant par exemple la branch "main" et en forcant la riview de code avant Pull Request

<p align="right">(<a href="#readme-top">retour en haut ⬆</a>)</p>
