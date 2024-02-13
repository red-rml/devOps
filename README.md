# DevOps  <a name="readme-top"></a>

## Auteurs 🎭

* **Bachekou DIABY** _alias_ [@Bachekou-DIABY](https://github.com/Bachekou-DIABY)
* **Rédouane RÉMILI** _alias_ [@FinOrfy](https://github.com/red-rml)


## Techno : 
* Docker
* Python
* Nginx
* MySQL
* Newman

### Présentation : 
- Montrer une partie de la réalisation technique
- Difficultés : Surmontés ou non 
- Ce qu’on retient

---

### Mise en place Etape 1 : Infra standard via Docker
- BDD MySQL qui run dans un conteneur docker
- Back python
- Serveur Nginx 
- Faire communiquer les services dans docker en les mettant tous dans le même network 


### Difficultés : Etape 1
* Faire communiquer les différents containers comme le back-end python et la bdd MySQL : 
  * Dans le fichier run.sh créer le network (sous-réseau) avec une IP fixe, avec à l’intérieur les différents services afin de permettre la communication entre ces services.

### Difficultés : Etape 2
* Installer Ansible : "Chemin source" "Chemin d’installation" 
  * Option -v et enter le chemin "absolu" source
* Faire fonctionner les commandes Ansible :
  * Il faut installer ansible directement dans le container ou il y a tout le projet avec la commande : ```apt-get install ansible```. Ensuite la commande ```ansible -v``` fonctionne.


### Ce qu’on retient 👍 

* Créer un network pour faire communiquer les différents service dans docker


<p align="right">(<a href="#readme-top">retour en haut ⬆</a>)</p>