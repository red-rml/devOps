# Crée le volume Nginx 

docker run --name devops-nginx-container -v /nginx/nginx.conf -d nginx

# crée le sous réseau 
docker network create --subnet=172.19.0.0/16 integrationNetwork

docker run --net integrationNetwork --ip 172.19.0.2 -dti --name devops-mysql-container devops-mysql-container