step 1: in the same path as the Dockerfile run ```docker build -t kangaroo .``` (don't miss the part to specify current directory)

step 2: ```docker run -d -it -p 5432:5432  --name=pg  kangaroo```

(optional step - i used the below step 3 to run queries against postgresql container - once running you can connect via browser and add server/db localhost or ip address, http://localhost:5555/browser/)

step 3: ```docker run -d -e PGADMIN_DEFAULT_EMAIL="karl” -e PGADMIN_DEFAULT_PASSWORD=“password” -p 5555:80 —name pgadmin dpage/pgadmin4```

step 4: run python load_data.py (i use pandas, glob,psycopg2, and os libraries so make sure they are installed. ```pip install -r requirements.txt```)
