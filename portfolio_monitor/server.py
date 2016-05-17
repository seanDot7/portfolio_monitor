# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(
    __name__,
    static_url_path='/static'
)

@app.route('/')
def getHomePage():
    return app.send_static_file('index.html')

def runServer(debug=False):
    if debug:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')

# back-end APIs
from mod_test.controllers import mod_test
from mod_position.controllers import mod_position

app.register_blueprint(mod_test)
app.register_blueprint(mod_position)

def main():
    app.run()

if __name__ == "__main__":
    main()
