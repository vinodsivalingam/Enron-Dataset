import os
from email.parser import Parser
import json
 
maindir = "C:\\Users\\Vinod\\Desktop\\Enron\\maildir"
keys_for_json = ["email_to","email_from","email_body"]
 
# Email is parsed and various contents of the email is extracted
def structure_email(file, email_to, email_from, email_body):
    with open(inputfile, "r") as f, open("out.json","w") as out:
        email_content = f.read()
    email = Parser().parsestr(email_content)
# Parsing individual items and creating a list of lists corresponds to a email
    email_to.append(email['to'])
    values_for_json.append(email_to)

    email_from.append(email['from'])
    values_for_json.append(email_from)

    email_body.append(email.get_payload())
    values_for_json.append(email_body)
 
#Zip function takes in two input lists(Keys, Values) and zip them into dictionary  
    json.dump(dict(zip(keys_for_json,values_for_json)),out)
    out.write("\n")
 
email_to = []
email_from = []
email_body = []
values_for_json = []
 
# Iterated through each mail in main directory
for directory, subdirectory, files in  os.walk(maindir):
    for file in files:
        structure_email(os.path.join(directory, file), email_to, email_from, email_body )
