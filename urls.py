import views


rules = [
    ('/', 'index', views.index),
    {
        'rule': '/home',
        'endpoint': 'home',
        'view_func': views.index},
    {
        'rule': '/sum/<int:x>/<int:y>',
        'endpoint': 'sum',
        'view_func': views.sum_xy
    },
    {
        'rule': '/sum/<int:x>',
        'endpoint': 'sum',
        'view_func': views.sum_xy
    },
    ('/google', 'google', views.google),
    ('/links', 'links', views.links),
    {
        'rule': '/data',
        'endpoint': 'data',
        'view_func': views.data,
        'methods': ['GET', 'POST', 'DELETE', 'PUT']
    }
]
