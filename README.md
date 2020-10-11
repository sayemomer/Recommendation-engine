# movie-recommendation-engine
        Version: 0.0.9 
        Authors: Omer Sayem

![](/src_img/python.ico?raw=true)

**ENVIRONMENT**


# Setup

* install dependencies: ```$ pip3 install -r requirements.txt```

* Start the server: ```$ python3 main.py```

* Start with Docker:
    ```$ docker build -t movie . ```
    ```$ docker run -p 5000:5000 movie```

# API endpoints

* Swagger API docs : 127.0.0.1:5000/apidocs

* Predict : 127.0.0.1:5000/predict?title=Toy Story

# TODO

- [ ] **More training set for better output**
- [ ] **API docs with swagger**
- [ ] **Client app**
- [ ] **Search engine**
- [ ] **Client app**
