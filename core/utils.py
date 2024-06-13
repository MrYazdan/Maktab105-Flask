def reserve(app, list_of_rule: list[dict | tuple]) -> None:
    for rule in list_of_rule:
        app.add_url_rule(*(rule if isinstance(rule, tuple) else rule.values()))
