from ext.configuration import *
from auth import routers
from jogo import routers

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_port'] = '3306'

app.secret_key = "asdokifhsAFHJQOIURHWEF'12983791283RQIGFE" 
app.run()
