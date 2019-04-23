from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
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
        <form method="post">
            <table>
                <tbody><tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </tbody></table>
            <input type="submit">
        </form>
    
    </body>
</html>
"""