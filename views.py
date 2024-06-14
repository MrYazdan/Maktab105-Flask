from flask import redirect, url_for, request, Response, render_template


def index():
    """Example endpoint returning a list of colors by palette
        This is using docstrings for specifications.
        ---
        definitions:
          Palette:
            type: object
            properties:
              palette_name:
                type: array
                items:
                  $ref: '#/definitions/Index'
          Color:
            type: string
        responses:
          200:
            description: A list of colors (maybe filtered by palette)
            schema:
              $ref: '#/definitions/Palette'
            examples:
              rgb: ['red', 'green', 'blue']
        """
    return render_template('home.html', user={
        'name': "alireza",
        'age': 20
    })


def sum_xy(x, y=10):
    return f"{x + y}"


def google():
    return redirect("https://google.com")


def links():
    return dict(
        index=url_for('index'),
        home=url_for('home'),
        links=url_for('links'),
        sum=url_for('sum', x=10),
        google=url_for('google'),
    )


def data():
    return dict(
        Method=request.method,
        Args=request.args,
        Url=request.url,
        Files=request.files,
        Form=request.form,
        Values=request.values,
        # Json=request.json,
        Headers={index: value for index, value in enumerate([*request.headers])}
    )


def str_html():
    return "<u><i>Salam Refigh</i></u>"


def dict_json():
    return {
        'key': 'value'
    }


def list_json():
    return ['ali', 'ashkan', 'fardin']


def hi():
    response = Response("<center><h1 style='color:red'>Salam</h1></center>", 200)
    return response
