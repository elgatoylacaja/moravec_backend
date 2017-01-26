from dennett.trials.api import trials
from dennett.stats.api import stats


def register_blueprints(app):
    app.register_blueprint(trials, url_prefix='/api/')
    app.register_blueprint(stats, url_prefix='/api/')
