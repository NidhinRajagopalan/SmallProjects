import pandas as pd
import datetime
import smtplib

#enter your mail details
GMAIL_ID = '' 
GMAIL_PSWD = ''

def sendEmail(to, sub, msg):
    print(f'Email to {to} sent with Subject: {sub} and message: {msg}')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f'Subject: {sub}\n\n{msg}')
    s.quit()

    
if __name__ == "__main__":
    # sendEmail(GMAIL_ID, 'subject', 'test message')
    # exit()
    df = pd.read_excel('bdayList.xlsx')
    today = datetime.datetime.now().strftime('%d-%m')
    yearCur = datetime.datetime.now().strftime('%Y')
    
    updateInd = []  #update the date to not wish again

    #to iterate through the datasheet considering 1 row
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime('%d-%m')

        if (today == bday) and yearCur not in str(item['Year']) :
            sendEmail(item['Email'], "HAPPY BIRTHDAY!", item['Wish'])
            updateInd.append(index) #appends the wished present year
        
    if updateInd:   #check if updateInd is empty 
        for i in updateInd:
            yr = df.loc[i, 'Year']
            df.loc[i, 'Year'] = str(yr) + ',' + str(yearCur)
        
    df.to_excel('bdayList.xlsx', index=False)
