from backend import routers
import os

app = routers.app
app.secret_key = "asdokifhsAFHJQOIURHWEF'12983791283RQIGFE" 
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
