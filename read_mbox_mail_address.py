import mailbox
import re
  
# Function to print Strings present 
# between any pair of delimiters 
def printSubstringInDelimiters(str):
    
    # Regex to extract the string 
    # between this two delimiters -> <>
    # If you have another delimiters you need to change the <>
    # from inside the regex variable to whatever you need
    regex = "\\<(.*?)\\>"
  
    # Find match between given string 
    # and regular expression 
    # using re.findall() 
    matches = re.findall(regex, str)

    # Some email doesn't have rìthe delimiters and they are already
    # printable
    if not matches:
        f_out.write("" + str + "\n")
  
    # Print the matches 
    for match in matches: 
        f_out.write("" + match + "\n") 

count = 0
mbox = mailbox.mbox("pathToTheMboxFile/INBOX.mbox")
f_out = open("email_address.txt", "w")

# The i index purpose is only to iterate the mbox list
for i, message in enumerate(mbox):
    count = count + 1
    printSubstringInDelimiters(message['from'])
    # If you want to print the subject of the email too
    # print("", message['subject'])

f_out.close()
print("Total emails: ", count)
