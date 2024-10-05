import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
cred = credentials.Certificate("path/to/your/firebase-admin-sdk.json")
firebase_admin.initialize_app(cred)

# Conectar a Firestore
db = firestore.client()

# Función para extraer datos
def extract_data():
    url = 'URL_DE_LA_PAGINA'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ajusta esto según la estructura de la tabla en la página
    table = soup.find('table')
    rows = table.find_all('tr')
    
    for row in rows[1:]:  # Saltar el encabezado
        cols = row.find_all('td')
        if cols:
            data = {
                'ciudad': cols[0].text,
                'codProducto': cols[1].text,
                'enviado': cols[2].text,
                'fechaCaptura': cols[3].text,
                'fechaCreacion': cols[4].text,
                'precioPromedio': cols[5].text,
                'producto': cols[6].text,
                'regId': cols[7].text,
            }
            # Subir datos a Firestore
            db.collection('tu_coleccion').add(data)

# Ejecutar la función
if __name__ == "__main__":
    extract_data()
