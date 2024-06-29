Directory Structure

api-project/
├── api/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
└── certbot/
    ├── init-letsencrypt.sh
    └── data/
        ├── certbot/
        └── www/

Initialize Let's Encrypt Certificates
Run the init-letsencrypt.sh script to generate and obtain TLS certificates:
cd certbot
chmod +x init-letsencrypt.sh
./init-letsencrypt.sh

Start the Services
Run docker-compose to start all the services defined in the docker-compose.yml file:
docker-compose up -d

