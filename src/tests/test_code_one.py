from ..code_one import Game, GameLibrary
from ..code_two import UserProfile

# Test Game class
def test_game_initialization():
    game = Game(
        name="Apex Legends",
        genre=["Shooter"],
        length_hours=20,
        difficulty="Advanced",
        platforms=["PC"],
        multiplayer=True
    )
    
    assert game.name == "Apex Legends"
    assert game.genre == ["Shooter"]
    assert game.length_hours == 20
    assert game.difficulty == "Advanced"
    assert game.platforms == ["PC"]
    assert game.multiplayer is True

# Test GameLibrary: add/remove
def test_add_game():
    library = GameLibrary()
    game = Game("Test", ["Action"], 10, "Beginner", ["PC"], True)

    library.add_game(game)

    assert len(library.games) == 1
    assert library.games[0].name == "Test"


def test_remove_game():
    library = GameLibrary()
    game = Game("Test", ["Action"], 10, "Beginner", ["PC"], True)

    library.add_game(game)
    library.remove_game(game)

    assert len(library.games) == 0

# Test GameLibrary.filter_games
def test_filter_games():
    # Create profile
    profile = UserProfile(
        preferred_genres=["Action"],
        max_game_length=30,
        skill_level="Intermediate",
        platforms=["PC", "PlayStation"],
        multiplayer_preference=False
    )

    # Create library + games
    library = GameLibrary()
    game1 = Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False)
    game2 = Game("Apex", ["Shooter"], 10, "Advanced", ["PC"], True)

    library.add_game(game1)
    library.add_game(game2)

    # Capture results
    filtered = library.filter_games(
        profile,
        filter_genre=True,
        filter_length=True,
        filter_skill=True,
        filter_platform=True,
        filter_multiplayer=True
    )

    # Should match only game1
    assert len(filtered) == 1
    assert filtered[0].name == "God of War"


# Test GameLibrary.rank_games
def test_rank_games():
    profile = UserProfile(
        preferred_genres=["Action"],
        max_game_length=40,
        skill_level="Intermediate",
        platforms=["PC"],
        multiplayer_preference=False
    )

    library = GameLibrary()

    game1 = Game("Action Game", ["Action"], 20, "Intermediate", ["PC"], False)
    game2 = Game("Nonmatch Game", ["Puzzle"], 50, "Beginner", ["Switch"], True)

    library.add_game(game1)
    library.add_game(game2)

    ranked_list = library.rank_games(profile)

    # ranked_list should be a list of tuples like (score, Game)
    assert isinstance(ranked_list, list)
    assert len(ranked_list) == 2

    # Highest score should be first
    assert ranked_list[0][1].name == "Action Game"
    assert ranked_list[0][0] > ranked_list[1][0]
