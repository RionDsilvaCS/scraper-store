from config import app
from google_playstore.google_playstore import google_playstore_blueprint
from app_store.app_store import app_store_blueprint

app.register_blueprint(google_playstore_blueprint, url_prefix='/google-playstore')
app.register_blueprint(app_store_blueprint, url_prefix='/app-store')

app.run()