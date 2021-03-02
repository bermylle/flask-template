from src import create_app,db

# Uncomment to deploy app to HEROKU
#app=create_app()

# Initiate DB 
db.create_all(app=create_app())