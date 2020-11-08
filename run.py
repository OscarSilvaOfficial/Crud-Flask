from backend.ext.configuration import getApp
from backend.auth import routers
from backend.jogo import routers

app = getApp()
app.secret_key = "asdokifhsAFHJQOIURHWEF12983791283RQIGFE" 

if __name__ == '__main__':
    app.run(debug=True)
    
