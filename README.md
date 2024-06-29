### **Directory Structure**

```Iomed
├── api
│   ├── app.py
│   ├── Dockerfile
│   └── requeriments.txt
├── certbot
│   └── init-letsencrypt.sh
├── docker-compose.yml
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── README.md
└── Technical Task DevOps.docx

4 directories, 9 files
```

### **Initialize Let's Encrypt Certificates**

Run the init-letsencrypt.sh script to generate and obtain TLS certificates:
```
cd certbot
chmod +x init-letsencrypt.sh
./init-letsencrypt.sh
```

### **Start the Services**

Run docker-compose to start all the services defined in the docker-compose.yml file:
```
docker-compose up -d
```
