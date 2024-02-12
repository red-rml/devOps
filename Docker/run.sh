
# crée le sous réseau 
docker network create --subnet=172.19.0.0/16 integrationNetwork

# Crée le volume Nginx 


docker run --net integrationNetwork --ip 172.19.0.2 -dti -p 3306:3306 --name devops-mysql-container devops-mysql-container

docker run --net integrationNetwork --ip 172.19.0.3 -dti -p 8000:8000 --name devops-python-container devops-python-container

docker run --net integrationNetwork --ip 172.19.0.4 --name devops-nginx-container -v /nginx/nginx.conf -d nginx
