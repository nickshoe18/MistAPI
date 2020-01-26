import smtplib
from email.mime.text import MIMEText

# =====
# Variables
# =====

mist_api_token = 'bD4syoPW3PJEQx6zznt3ao3xVa8vkPqgS090AtkDPOFauP0hhUexPw3iwmKq1he7nwL3cGug4quPlfanoc1WVwEocW42KSzs'

org_id = '3896a314-69a7-4ecb-b1ca-b9e9a99c3549'

site_id = 'afbdf51c-a089-4a27-8197-afe851a1ddcf'

headers = {
    'Content-Type': 'applications/json',
    'Authorization': 'Token ' + mist_api_token
}

gmail_id = 'nshoe18@gmail.com'
gmail_password = 'R0y@ls520'
'''
Send email.
Note: Goodle bloks sign-in attempts from apps which do not
use modern security standards or do not support your two-step
verification requirements.
Documentation:
https://support.google.com/accounts/answer/6009563
You can allow less secure apps here:
https://www.google.com/settings/security/lesssecureapps
You can bypass the next Captcha here:
https://accounts.google.com/b/0/DisplayUnlockCaptcha
'''


def send_email(recipient, subject='', body='', message_type='plain'):
    try:
        print('Sending email to {}...'.format(recipient))

        msg = MIMEText(body, message_type)
        msg['Subject'] = subject
        msg['From'] = gmail_id
        msg['To'] = ', '.join(recipient) if isinstance(recipient, list) else recipient

        server = smtplib.SMTP_SSL('smtp.google.com', 465)
        server.login(gmail_id, gmail_password)
        server.sendmail(gmail_id, ', {}'.join(recipient) if isinstance(recipient, list) else recipient,
        msg.as_string())
        server.close()
    except Exception as e:
        print('Failed to send email:')
        print(e)

        return

    print('Successfully sent email')
