from datetime import datetime
import random
from django.core.mail import send_mail

class CustomEmailService :
    def sendAuth(userEmailAddr, randNum) :
        print(userEmailAddr, randNum)
        return send_mail(
            subject='[조이풀] 관리자 페이지 이동을 위한 인증번호입니다.',  # Email subject
            message= str(randNum),  # Email body
            from_email='yujin_career@naver.com',  # Sender's email
            recipient_list=[userEmailAddr],  # List of recipients
            fail_silently=False,  # Raise exception if sending fails
        )

    def sendRecoverRequest(content, ipAdress, requestingPerson):
        try:
            subject = "[조이풀] 관리자 인증 로그인에 문제를 겪고 있습니다"

            # Get today's date as a string
            requesting_time = datetime.date.today().strftime("%Y-%m-%d")

            # HTML message (Using f-strings for better readability)
            html_message = f"""
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0;">
                <div style="max-width: 600px; margin: 20px auto; background: #ffffff; padding: 20px; 
                            border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                    <div style="text-align: center; font-size: 16px; color: #333;">
                        <h2 style="margin-bottom: 10px;">Error Detail of Joyful</h2>
                        <p style="margin-bottom: 15px;"><strong>CONTENT:</strong> {content}</p>
                        <p style="margin-bottom: 15px;"><strong>IP ADDRESS:</strong> {ipAdress}</p>
                        <p style="margin-bottom: 15px;"><strong>REQUESTING PERSON:</strong> {requestingPerson}</p>
                        <p style="margin-bottom: 15px;"><strong>REQUESTING TIME:</strong> {requesting_time}</p>
                    </div>
                </div>
            </body>
            """

            # Send the email
            return send_mail(
                subject=subject,  # Email subject
                message="",  # Leave plain text empty (not used)
                from_email='yujin_career@naver.com',  # Sender's email
                recipient_list=["cuu2252@gmail.com"],  # List of recipients
                fail_silently=False,  # Raise exception if sending fails
                html_message=html_message  # Use the HTML message
            )

        except Exception as e:
            print(f"Error sending email: {e}")
            return False  # Return False if the email fails to send