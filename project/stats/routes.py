import pandas as pd
from flask import current_app, render_template, request

import app
from . import stats_blueprint


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


@stats_blueprint.route('/_png_plot', methods=['GET', 'POST'])
def png_plot():
    current_app.logger.info('Calling the png_plot() function.')

    return render_template('stats/png_plot.html')


@stats_blueprint.route('/_opening_explorer', methods=['GET', 'POST'])
def opening_explorer():
    current_app.logger.info('Calling the opening_explorer() function.')

    df = app.uf.get_explorer_table()

    # get table headers and rows
    columns = df.columns
    rows = df.values

    # re-render html page with new table values
    return render_template('stats/opening_explorer.html',
                           columns=columns,
                           rows=rows)


@stats_blueprint.route('/_update_alternative_elo_table', methods=['GET', 'POST'])
def update_alternative_elo_table():
    elo = int(list(request.args.values())[0])
    white_value = list(request.args.values())[1] == 'true'

    # get new dataframe based on new elo value
    if white_value:
        df = app.uf.get_recommend_w(elo)
    else:
        df = app.uf.get_recommend_b(elo)

    # return the new table out to the client
    return pd.DataFrame(df).to_json(orient='columns')


@stats_blueprint.route('/_elo_opening_suggestion', methods=['GET', 'POST'])
def elo_opening_suggestion():
    current_app.logger.info('Calling the elo_opening_suggestion() function.')

    # re-render html page with new table values
    return render_template('stats/elo_opening_suggestion.html')


@stats_blueprint.route('/_update_opening_suggester_table', methods=['GET', 'POST'])
def update_opening_suggester_table():
    skill = int(list(request.args.values())[0])
    novelty = int(list(request.args.values())[1])
    white_value = list(request.args.values())[2] == 'true'

    # get new dataframe based on new elo value
    if white_value:
        df = app.uf.get_ad_recommend_w(skill, novelty)
    else:
        df = app.uf.get_ad_recommend_b(skill, novelty)

    # return the new table out to the client
    return pd.DataFrame(df).to_json(orient='columns')


@stats_blueprint.route('/_opening_suggester_page', methods=['GET', 'POST'])
def opening_suggester_page():
    current_app.logger.info('Calling the opening_suggester_page() function.')

    # re-render html page with new table values
    return render_template('stats/opening_suggester.html')


@stats_blueprint.route('/', methods=['GET', 'POST'])
def index():
    current_app.logger.info('Calling the index() function.')

    # re-render html page with new table values
    return render_template('stats/opening_suggester.html')
