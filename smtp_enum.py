import os
def open_resources(file_path):
    return [item.replace("\n", "") for item in open(file_path).readlines()]
wordlist = open_resources("emails")

for emails in wordlist:
        print "\n[+]Sending email to " + emails
        command = 'swaks --from "fakemail@smtp.enum" --body "http://10.10.14.38:8080" --to ' + emails + " > /dev/null"
        #print command
        os.system(command)
