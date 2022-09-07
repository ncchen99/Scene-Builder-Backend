# Scene Builder 

### Steps

1. Setting environment variables:
```bash
export USERNAME=[你要設定的 mongodb 帳號，沒有中括號]
export PASSWORD=[你要設定的 mongodb 密碼，沒有中括號]
```

2. Deploy via [Docker compose](https://docs.docker.com/compose/)🚀
```bash
sudo -E docker compose up -d
```
<!--
1. Create `.env` file and configure as:
   
    ```bash
    USERNAME=[你要設定的 mongodb 帳號，沒有中括號]
    PASSWORD=[你要設定的 mongodb 密碼，沒有中括號]
    ```
2. `sudo docker compose up -d`

3. `sudo docker build --tag flask-docker . ` 
4. `sudo docker run -d -p 5000:5000 flask-docker`
-->
