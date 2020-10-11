from server import Server
from model import TfidfModel

if __name__ == '__main__':
    TfidfModel().vectorization()
    Server().run()