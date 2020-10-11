FROM continuumio/anaconda3:4.4.0
COPY . /usr/local/movie/
EXPOSE 5000
WORKDIR /usr/local/movie/
RUN pip install -r requirements.txt
CMD python main.py