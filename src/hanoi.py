from dataclasses import dataclass, field


@dataclass(frozen=True)
class Move:
    """Representa um único movimento de disco entre dois pinos."""

    disk: int
    source: str
    target: str


class InvalidMoveError(ValueError):
    """Exceção lançada quando um movimento viola as regras da Torre de Hanói."""


@dataclass
class HanoiGame:
    """Motor lógico da Torre de Hanói usando listas como pilhas (LIFO)."""

    num_disks: int
    rods: dict[str, list[int]] = field(init=False)
    history: list[Move] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        if self.num_disks < 1:
            raise ValueError("A quantidade de discos deve ser maior ou igual a 1.")

        # Maior disco fica na base (índice 0) e menor disco fica no topo (último elemento).
        self.rods = {
            "A": list(range(self.num_disks, 0, -1)),
            "B": [],
            "C": [],
        }

    def can_move(self, source: str, target: str) -> bool:
        """Verifica se é possível mover o disco do topo de `source` para `target`."""
        if source not in self.rods or target not in self.rods:
            return False
        if source == target:
            return False
        if not self.rods[source]:
            return False

        moving_disk = self.rods[source][-1]
        if self.rods[target] and self.rods[target][-1] < moving_disk:
            return False

        return True

    def move_disk(self, source: str, target: str) -> Move:
        """Executa o movimento de um disco entre pinos ou lança InvalidMoveError."""
        if not self.can_move(source, target):
            raise InvalidMoveError(f"Movimento inválido de '{source}' para '{target}'.")

        disk = self.rods[source].pop()
        self.rods[target].append(disk)

        move = Move(disk=disk, source=source, target=target)
        self.history.append(move)
        return move

    def is_solved(self, target_rod: str = "C") -> bool:
        """Verifica se todos os discos estão ordenados no pino de destino."""
        if target_rod not in self.rods:
            return False
        expected = list(range(self.num_disks, 0, -1))
        return self.rods[target_rod] == expected

    @property
    def move_count(self) -> int:
        """Retorna a quantidade de movimentos realizados até o momento."""
        return len(self.history)

    @staticmethod
    def expected_min_moves(num_disks: int) -> int:
        """Retorna o número mínimo teórico de movimentos: 2^n - 1."""
        if num_disks < 1:
            raise ValueError("A quantidade de discos deve ser maior ou igual a 1.")
        return (2**num_disks) - 1


def solve_hanoi_recursive(
    num_disks: int,
    source: str = "A",
    target: str = "C",
    auxiliary: str = "B",
    moves: list[Move] | None = None,
) -> list[Move]:
    """Gera a sequência ótima de movimentos da Torre de Hanói via recursão."""
    if num_disks < 1:
        raise ValueError("A quantidade de discos deve ser maior ou igual a 1.")

    if moves is None:
        moves = []

    if num_disks == 1:
        moves.append(Move(disk=1, source=source, target=target))
        return moves

    solve_hanoi_recursive(num_disks - 1, source, auxiliary, target, moves)
    moves.append(Move(disk=num_disks, source=source, target=target))
    solve_hanoi_recursive(num_disks - 1, auxiliary, target, source, moves)
    return moves
