from backend.ext.configuration import *
from backend.auth import routers
from backend.jogo import routers

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_port'] = '3306'

app.secret_key = "asdokifhsAFHJQOIURHWEF'12983791283RQIGFE" 

if __name__ == '__main__':
    app.run(debug=True)
