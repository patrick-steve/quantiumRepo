from dash.testing.application_runners import import_app

def test_app001(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    assert dash_duo.find_element("H1").text == "Sales Price Graph"
    return None

def test_app002(dash_duo):
    app = import_app('app')
    dash_duo.start_server(app)

    assert dash_duo.find_element('#region-selector')
    return None

def test_app003(dash_duo):
    app = import_app('app')
    dash_duo.start_server(app)

    assert dash_duo.find_element('#sales_graph')
    return None