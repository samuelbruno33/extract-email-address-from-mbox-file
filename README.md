# extract-email-address-from-mbox-file
This python script allows you to extract all the email addresses contained in a mbox file and write them inside a text file.

Usually the mail addresses in a mbox file can be of the type:
PersonName <email@example.com> or <email@example.com> or just email@example.com

There are 3 possible cases where the delimiters for the email address are <> or only the address is present.

This script allows you to print only what is inside the delimiters (if you have different delimiters just change the delimiter variable within the script), while if a line has no delimiters then it means that only an email address is present.
