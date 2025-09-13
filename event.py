import re
from dbController import run_query
from langsmith import traceable  
# Simple in-memory user list
user_db = []

def extract_username(text):
    match = re.search(r"user(?: named| with name)? (\w+)", text, re.IGNORECASE)
    return match.group(1) if match else None


def cameras_to_html_response(cameras):
    html = """
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>Camera Name</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
    """
    for cam_name, desc in cameras:
        html += f"        <tr><td>{cam_name}</td><td>{desc}</td></tr>\n"
    
    html += """      </tbody>
    </table>
    """
    return html.strip()

@traceable(name="Handle event execution")
def handle_event(intent, text):
    username = extract_username(text)

    if intent == 'create_user':
        '''if not username:
            return "Please specify the user name to create."
        if username in user_db:
            return f"User '{username}' already exists."
        user_db.append(username)
        return f"User '{username}' has been created."'''
        return run_query(text)

    elif intent == 'delete_user':
        '''if not username:
            return "Please specify the user name to delete."
        if username not in user_db:
            return f"User '{username}' does not exist."
        user_db.remove(username)'''
        run_query(text)
        return f"User '{username}' has been deleted."

    elif intent == 'list_users':
        '''if not user_db:
            return "No users found."
        return "Users in the system:\n" + "\n".join(f"- {user}" for user in user_db)'''
        output = run_query(text)
        return output
        #return run_query(text)
    
    elif intent == 'create_camera':
        '''create camera in the database'''
        return run_query(text)
    
    elif intent == 'delete_camera':
        '''delete camera from the database'''
        return run_query(text)
    
    elif intent == 'list_camera':
        '''fetch all the camera from the database'''
        cameras = [
            ("Cam1", "Cam Desc 1"),
            ("cam2", "Cam Desc 2"),
            ("HonCamera", "Cam Desc 3"),
            ("S2 Camera", "Cam Desc 4"),
            ("Lenel Camere ", "Cam Desc 5")
        ]

        html_response = cameras_to_html_response(cameras)

        return html_response
        #return run_query(text)
    else:
        return "Unsupported user operation."
