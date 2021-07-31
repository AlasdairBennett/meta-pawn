import utility_functions as uf
from project import create_app

app = create_app()

# Global variables to be piped through routes.py to be displayed on front end
chess_games = uf.get_games('project/static/games.csv')
