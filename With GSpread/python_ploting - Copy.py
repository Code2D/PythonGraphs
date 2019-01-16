print('[ * ] Loading Imports')

# Imports
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print('[ * ] Loaded Modules')

# Setting up connection to Google Sheet

print('[ * ] Connecting to server') #Logs Progress

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)
sheet = client.open('PythonGraphsData').sheet1

print(sheet.cell(2,4).value)

scan = 1

samplesize = 0

X_Axis = []

Y_Axis = []

while scan == 1:
    if sheet.cell(samplesize + 1, 2).value == "end":
        scan = 0
    else:
        samplesize += 1
        X_Axis.append(sheet.cell(samplesize, 2).value)
        print(sheet.cell(samplesize, 2).value)

print ("outside While?")
samplesize = 0
scan = 1

while scan == 1:
    if sheet.cell(samplesize + 1, 2).value == "end":
        scan = 0
    else:
        samplesize += 1
        Y_Axis.append(sheet.cell(samplesize, 2).value)
        print(sheet.cell(samplesize, 2).value)

# Describing data
plt.plot(X_Axis, Y_Axis)

# Defining Graph
plt.ylabel('Population')
plt.xlabel('Year')
plt.title("New Zealand's Population Growth")
plt.show()

# Console Messages
print('[ * ] Plot Compilied')
