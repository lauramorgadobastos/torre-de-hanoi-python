import pytest

from src.hanoi import HanoiGame, InvalidMoveError, Move, solve_hanoi_recursive


def test_initial_game_state():
    game = HanoiGame(num_disks=3)

    assert game.num_disks == 3
    assert game.rods == {
        "A": [3, 2, 1],
        "B": [],
        "C": [],
    }
    assert game.history == []
    assert game.move_count == 0
    assert not game.is_solved("C")


@pytest.mark.parametrize("invalid_disks", [0, -1, -5])
def test_invalid_num_disks_raises_value_error(invalid_disks: int):
    with pytest.raises(ValueError):
        HanoiGame(num_disks=invalid_disks)


def test_valid_move_updates_stacks_and_history():
    game = HanoiGame(num_disks=3)

    move = game.move_disk("A", "C")

    assert move == Move(disk=1, source="A", target="C")
    assert game.rods["A"] == [3, 2]
    assert game.rods["C"] == [1]
    assert game.move_count == 1
    assert game.history == [move]


def test_cannot_place_larger_disk_on_smaller_disk():
    game = HanoiGame(num_disks=3)
    game.move_disk("A", "B")  # disco 1 vai para B

    assert not game.can_move("A", "B")  # disco 2 não pode ir sobre o disco 1
    with pytest.raises(InvalidMoveError):
        game.move_disk("A", "B")
    assert game.move_count == 1


@pytest.mark.parametrize(
    ("source", "target"),
    [
        ("B", "A"),  # pino de origem vazio
        ("A", "A"),  # mesmo pino
        ("X", "A"),  # pino inexistente
        ("A", "Z"),  # pino destino inexistente
    ],
)
def test_invalid_moves_raise_error(source: str, target: str):
    game = HanoiGame(num_disks=2)

    assert not game.can_move(source, target)
    with pytest.raises(InvalidMoveError):
        game.move_disk(source, target)


@pytest.mark.parametrize(
    ("num_disks", "expected_moves"),
    [
        (1, 1),
        (2, 3),
        (3, 7),
        (4, 15),
        (5, 31),
    ],
)
def test_expected_min_moves(num_disks: int, expected_moves: int):
    assert HanoiGame.expected_min_moves(num_disks) == expected_moves


@pytest.mark.parametrize("invalid_n", [0, -3])
def test_expected_min_moves_invalid_raises_value_error(invalid_n: int):
    with pytest.raises(ValueError):
        HanoiGame.expected_min_moves(invalid_n)


def test_solve_hanoi_recursive_for_three_disks():
    moves = solve_hanoi_recursive(num_disks=3, source="A", target="C", auxiliary="B")

    assert len(moves) == 7
    assert moves[0] == Move(disk=1, source="A", target="C")
    assert moves[-1] == Move(disk=1, source="A", target="C")


@pytest.mark.parametrize("num_disks", [1, 2, 3, 4])
def test_recursive_solution_solves_game_cleanly(num_disks: int):
    game = HanoiGame(num_disks=num_disks)
    moves = solve_hanoi_recursive(num_disks=num_disks, source="A", target="C", auxiliary="B")

    for move in moves:
        game.move_disk(move.source, move.target)

    assert game.is_solved("C")
    assert game.move_count == HanoiGame.expected_min_moves(num_disks)
