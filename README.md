Google Docs API https://developers.google.com/sheets/

Guide on Setting Up Google API https://youtu.be/3wC-SCdJK2c?si=LAnge3P9hJWu8Vmu

Google Developers Console https://console.cloud.google.com/cloud-resource-manager?pli=1

Requirements: pip install google-api-python-client httplib2 oauth2client selenium webdriver_manager

File "readfromsheet.py" retrieves values from the table and writes them to the "id_products.txt" file. 
File "parser.py" parses the website using the values from the "id_products.txt" file. 
File "writetosheet.py" writes values from the "charvalues.txt" file to the table.
