import app
from . import stats_blueprint
from flask import current_app, render_template


# request callbacks
@stats_blueprint.before_request
def stats_before_request():
    current_app.logger.info('Calling before_request() for the stats blueprint...')


@stats_blueprint.after_request
def stats_after_request(response):
    current_app.logger.info('Calling after_request() for the stats blueprint...')
    return response


@stats_blueprint.teardown_request
def stats_teardown_request(error=None):
    current_app.logger.info('Calling teardown_request() for the stats blueprint...')


@stats_blueprint.route('/')
def index():
    current_app.logger.info('Calling the index() function.')
    return render_template('stats/index.html',
                           chesstable=[app.chess_games.to_html(index=False)],
                           titles=app.chess_games.columns.values)
