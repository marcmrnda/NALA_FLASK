from NALA__web import main
from flask import session

app = main()

print(app.url_map)  

if __name__ == '__main__':
    app.run()