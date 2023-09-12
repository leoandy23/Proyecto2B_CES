import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("proyecto-ces-eb82b-firebase-adminsdk-y17i7-d74365d76f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def create_person(name, last_name, age, semester, career):
    doc_ref = db.collection('persons').document()
    doc_ref.set({
        'name': name,
        'last_name': last_name,
        'age': age,
        'semester': semester,
        'career': career
    })

def get_persons():
    docs = db.collection('persons').stream()
    persons = []
    for doc in docs:
        persons.append(doc.to_dict())
    return persons

def get_person_by_id(id):
    doc = db.collection('persons').document(id).get()
    return doc.to_dict()

def update_person(id, data):
    doc_ref = db.collection('persons').document(id)
    doc_ref.update(data)

def delete_person(id):
    db.collection('persons').document(id).delete()

def get_person_by_semester(semester):
    semester = int(semester)
    docs = db.collection('persons').where('semester', '==', semester).stream()
    persons = []
    for doc in docs:
        persons.append(doc.to_dict())
    return persons
