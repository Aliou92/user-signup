from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
html_Header ="""
<html>
    <head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
"""
user_Username ="""
        <form action = "/add_values" method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" id="username" type="text" value>
                    </td>
                </tr>
"""                
user_Password ="""                
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" id="password" type="password" value>
                    </td>
                </tr>
                 <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" id="verify" value>
                    </td>
                </tr>
"""
user_Email ="""               
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" id="email" value>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
""" 
html_Footer ="""       
    </body>    
</html>
"""

@app.route("/add_values", methods = ['GET','POST'])
def add_user():
    new_username = request.form['username']
    new_password = request.form['password']
    verify_password = request.form['verify'] 
    email_address = request.form['email']

    success = True

    html_Header ="""
    <html>
        <head>
            <style>
                .error {
                    color: red;
                }
            </style>
        </head>
        <body>
        <h1>Signup</h1>
    """    

    user_Username ="""
            <form action = "/add_values" method="post">
                <table>
                    <tr>
                        <td><label for="username">Username</label></td>
                        <td>
                            <input name="username" id="username" type="text" value>
                        </td>
                    </tr>
    """  
    user_Password ="""                
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td>
                            <input name="password" id="password" type="password" value>
                        </td>
                    </tr>            
                    <tr>
                        <td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" id="verify" type="password" value>
                        </td>
                    </tr>
    """

    user_Email ="""               
                    <tr>
                        <td><label for="email">Email (optional)</label></td>
                        <td>
                            <input name="email" id="email" value>
                        </td>
                    </tr>
                </table>
                <input type="submit">
            </form>
    """

    if new_username == '':
        user_Username = """
        <form action = "/add_values" method="post">
                <table>
                    <tr>
                        <td><label for="username">Username</label></td>
                        <td>
                            <input name="username" type="text" id="username" value>
                            <span class="error"> Username is not valide </span>
                        </td>
                    </tr>
        """
        success = False

    if new_password == '':
        user_Password ="""                
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td>
                            <input name="password" id="password" type="password" value>
                            <span class="error"> Password is not valide </span>
                        </td>
                    </tr>
                    <tr>
                        <td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" id="verify" type="password" value>
                        </td>
                    </tr>
        """
        success = False

    if len(new_password) < 3 or len(new_password) > 20:
        user_Password ="""                
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td>
                            <input name="password" id="password" type="password" value>
                            <span class="error"> Number of character is not valid</span>
                        </td>
                    </tr>
                    <tr>
                        <td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" type="password" id="verify" value>
                        </td>
                    </tr>
        """
        success = False
        
    if verify_password =='':
        user_Password ="""                
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td>
                            <input name="password" id="password" type="password" value >
                        </td>
                    </tr>
                    <tr>
                        <td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" type="password" id="verify" value>
                            <span class ="error"> Password are not the same </span>
                        </td>
                    </tr>
        """ 
        success = False


    elif new_password != verify_password:
        user_Password ="""                
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td>
                            <input name="password" id="password" type="password" value>
                        </td>
                    </tr>
                    <tr>
                        <td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" type="password" id="verify" value>
                            <span class ="error"> Password are not the same </span>
                        </td>
                    </tr>
        """ 
        success = False

    if '@' not in  email_address and '.' not in email_address or email_address =='':
        user_Email ="""               
                    <tr>
                        <td><label for="email">Email (optional)</label></td>
                        <td>
                            <input name="email" id="email" type="text" value>
                            <span class="error"> email is not valide </span>
                        </td>
                    </tr>
                </table>
                <input type="submit">
            </form>
        """ 
        success = False     



    content = html_Header + user_Username + user_Password + user_Email + html_Footer

    if success == True:
        content = """
            <!DOCTYPE html>
                <html>
                    <head>
                    </head>
                    <style>
                        .success {
                            font: impact;
                            font-size: 50px;
                            
                        }
                    </style>
                    <body>
                        <h1 class="success">Welcome, """ + new_username + """!</h1>
                    </body>
                </html>   
                """                            

    return content



@app.route("/", methods=['GET', 'POST'])
def index():
    html_signup = html_Header + user_Username + user_Password + user_Email + html_Footer
    return html_signup

app.run()    







