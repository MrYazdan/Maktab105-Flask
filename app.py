from flask import Flask, redirect, url_for
from core.utils import reserve
from urls import rules

app = Flask("Maktab_105")

# serving url patterns
reserve(app, rules)

@app.route('/google')
def google():
    return redirect("https://google.com")


@app.route('/links')
def links():
    return dict(
        index=url_for('index'),
        home=url_for('home'),
        links=url_for('links'),
        sum=url_for('sum', x=10),
        google=url_for('google'),
    )



if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
