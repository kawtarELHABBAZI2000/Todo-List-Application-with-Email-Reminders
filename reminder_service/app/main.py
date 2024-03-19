from email.message import EmailMessage
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from postmarker.core import PostmarkClient
from datetime import datetime

load_dotenv()

app = FastAPI()

POSTMARK_SERVER = os.getenv("POSTMARK_SERVER")
POSTMARK_PORT = int(os.getenv("POSTMARK_PORT"))
POSTMARK_USERNAME = os.getenv("POSTMARK_USERNAME")
POSTMARK_PASSWORD = os.getenv("POSTMARK_PASSWORD")

@app.post("/send_reminder_email")
def send_reminder_email(task_details):

    # Sends a reminder email using the Postmark API.

    # Args:
    #     task_details (dict): Details of the task including task name, description, due date, status, and recipient's email.

    # Returns:
    #     dict: A message indicating the success or failure of the email sending process.

    try:
        postmark = PostmarkClient(server_token=POSTMARK_USERNAME)
        formatted_due_date = datetime.strptime(task_details.due_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")

        # Create dynamic content using task_details
        html_body = f"""
            <html>
                <body>
                    <strong>Hello</strong> dear Postmark user,<br><br>
                    Task: {task_details.task}<br>
                    Description: {task_details.description}<br>
                    Due Date: {formatted_due_date}<br>
                    Status: {task_details.status}
                </body>
            </html>
        """
        # Create an Email object with relevant details
        email = postmark.emails.Email(
            From='user@paylik.ma',
            To= task_details.to_email,
            Subject= f"""Reminder: {task_details.task}""",
            HtmlBody= html_body
        )
        email['X-PM-Message-Stream'] = 'outbound'

        email.send()
    except Exception as e:
        print(e)
        return {"message": "Reminder email failed to send."}
    
    return {"message": "Reminder email sent successfully!"}