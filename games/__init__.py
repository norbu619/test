"""Initialize Flask app."""

from flask import Flask, render_template

from games.browse import services
# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from games.domainmodel.model import Game
import games.adapters.repository as repo
from games.adapters.memory_repository import populate
from games.adapters.memory_repository import MemoryRepository


# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
def create_some_game():
    some_game = Game(1, "Call of Duty® 4: Modern Warfare®")
    some_game.release_date = "Nov 12, 2007"
    some_game.price = 9.99
    some_game.description = "The new action-thriller from the award-winning team at Infinity Ward, the creators of " \
                            "the Call of Duty® series, delivers the most intense and cinematic action experience ever. "
    some_game.image_url = "https://cdn.akamai.steamstatic.com/steam/apps/7940/header.jpg?t=1646762118"
    return some_game


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    with app.app_context():
        from .browse import browse
        app.register_blueprint(browse.browse_blueprint)

    repo.repo_instance = MemoryRepository()
    populate(repo.repo_instance)

    # Create the Flask app object.

    @app.route('/')
    def home():
        some_game = create_some_game()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
        return render_template('gameDescription.html', game=some_game, gzz = services.get_g(repo.repo_instance))

    return app

