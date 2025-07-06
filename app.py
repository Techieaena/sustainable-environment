from flask import Flask, request, redirect, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('webpage.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Collect form data
        data = {
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'company': request.form['company'],
            'zip': request.form['zip'],
            'country': request.form['country'],
            'purpose': request.form['purpose'],
            'referral': request.form.get('referral', ''),
            'comments': request.form.get('comments', '')
        }

        # Format the email body
        message_body = f"""
New Contact Form Submission:

Name: {data['firstname']} {data['lastname']}
Email: {data['email']}
Phone: {data['phone']}
Company: {data['company']}
Zip Code: {data['zip']}
Country: {data['country']}
Purpose: {data['purpose']}
Referral: {data['referral']}
Comments: {data['comments']}
"""

        # Compose and send email
        msg = MIMEText(message_body)
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = 'aenkhich@gmail.com'
        msg['To'] = 'aenkhich@gmail.com'

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('aenkhich@gmail.com', 'tyvc wspi exqx bhpu')  # app password
                smtp.send_message(msg)
                print("✅ Email sent successfully.")
        except Exception as e:
            print(f"❌ Email sending failed: {e}")

        return redirect('/thankyou')

    return render_template('form.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
