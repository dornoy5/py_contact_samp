import json

contacts = [{"name": "waga", "tel": "123"}]

def save_2_file():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def load_from_file():
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    return contacts

if __name__ == "__main__":
    save_2_file()
    contacts = load_from_file()
    print(contacts)

