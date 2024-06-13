import views

# @app.route('/sum/<int:x>', defaults={'y': 10})

rules = [
    ('/', 'index', views.index),
    {
        'rule': '/home',
        'endpoint': 'home',
        'view_func': views.index},
    {
        'rule': '/sum/<int:x>/<int:y>',
        'endpoint': 'sum', 'view_func':
        views.sum_xy
    },
    {
        'rule': '/sum/<int:x>',
        'endpoint': 'sum', 'view_func':
        views.sum_xy
    },

]
