Contact_list = [
{"name":"Emeka","phone":"08147480937","email":"alifojohnson@gmail.com"},
{"name":"Praise","phone":"09136914694","email":"ifeanyiozioma2019@gmail.com"},
{"name":"Amara","phone":"08115363690","email":"ifeanyiamarachi@gmail.com"}]
def print_contact_list():
    for contact in Contact_list:    
        print(f"{contact['name']} with phone number {contact['phone']} and email {contact['email']}.")
    print_contact_list()    
    
def edit_contact([index, field, value]):
if index < 1 or index > len(contact_list):
    print("E no go work, invalid contact index.")
    
elif field not in Contacts[0].keys():
    print("invalid field name, try again")
