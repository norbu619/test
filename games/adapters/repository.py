import abc
from typing import List
from games.domainmodel.model import Game, Genre

repo_instance = None


class RepositoryException(Exception):
    def __int__(self, message=None):
        print(f"RepositoryException: {message}")


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_game(self, game: Game):
        raise NotImplementedError

    @abc.abstractmethod
    def get_games(self) -> List[Game]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_games(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        raise NotImplementedError
