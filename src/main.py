from src.hanoi import HanoiGame, InvalidMoveError, solve_hanoi_recursive


class QuitGameError(Exception):
    """Exceção interna usada para encerrar o modo manual a pedido do usuário."""


def prompt_int(message: str, min_value: int = 1, max_value: int = 8) -> int:
    """Solicita um número inteiro dentro do intervalo permitido."""
    while True:
        raw_value = input(message).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        if value < min_value or value > max_value:
            print(f"Digite um número entre {min_value} e {max_value}.")
            continue

        return value


def prompt_rod(message: str, allow_quit: bool = False) -> str:
    """Solicita um pino válido (A, B ou C) e, se permitido, aceita sair."""
    valid_rods = ("A", "B", "C")
    quit_commands = ("S", "SAIR", "Q", "QUIT")

    while True:
        choice = input(message).strip().upper()
        if allow_quit and choice in quit_commands:
            raise QuitGameError()
        if choice in valid_rods:
            return choice

        if allow_quit:
            print("Pino inválido. Escolha entre A, B, C ou digite 'S' para sair.")
        else:
            print("Pino inválido. Escolha entre A, B ou C.")


def render_board(game: HanoiGame) -> str:
    """Gera uma representação visual em modo texto dos pinos e discos."""
    max_disk = game.num_disks
    # Largura máxima de um disco: '[' + espaço + (2*max_disk - 1) '=' + espaço + ']'
    cell_width = (2 * max_disk) + 3
    lines: list[str] = []

    # Desenha de cima para baixo (do índice max_disk - 1 até 0)
    for level in range(max_disk - 1, -1, -1):
        row_parts: list[str] = []
        for rod_name in ("A", "B", "C"):
            stack = game.rods[rod_name]
            if level < len(stack):
                disk = stack[level]
                equals = "=" * ((2 * disk) - 1)
                token = f"[ {equals} ]"
            else:
                token = "|"
            row_parts.append(token.center(cell_width))
        lines.append("  ".join(row_parts))

    # Base e rótulos dos pinos
    base_width = (cell_width * 3) + 4
    lines.append("-" * base_width)

    labels = [rod_name.center(cell_width) for rod_name in ("A", "B", "C")]
    lines.append("  ".join(labels))
    lines.append(f"Movimentos realizados: {game.move_count}")

    return "\n".join(lines)


def run_automatic_mode(num_disks: int) -> None:
    """Executa e exibe a solução recursiva passo a passo."""
    game = HanoiGame(num_disks=num_disks)
    moves = solve_hanoi_recursive(num_disks=num_disks, source="A", target="C", auxiliary="B")

    print("\n--- Estado inicial ---")
    print(render_board(game))

    for step, move in enumerate(moves, start=1):
        input("\nPressione Enter para o próximo passo...")
        game.move_disk(move.source, move.target)
        print(
            f"\nPasso {step}/{len(moves)}: mover disco {move.disk} "
            f"de {move.source} -> {move.target}"
        )
        print(render_board(game))

    print(
        f"\nConcluído em {game.move_count} movimentos "
        f"(mínimo teórico: {game.expected_min_moves(num_disks)})."
    )


def run_manual_mode(num_disks: int) -> None:
    """Permite que o usuário mova os discos manualmente até resolver ou sair."""
    game = HanoiGame(num_disks=num_disks)
    print("\nObjetivo: mover todos os discos de 'A' para 'C' sem colocar disco maior sobre menor.")
    print("Dica: digite 'S' (ou 'sair') a qualquer momento para encerrar a partida.")

    try:
        while not game.is_solved("C"):
            print("\n" + render_board(game))
            source = prompt_rod("Pino de origem (A/B/C ou S para sair): ", allow_quit=True)
            target = prompt_rod("Pino de destino (A/B/C ou S para sair): ", allow_quit=True)

            try:
                move = game.move_disk(source, target)
                print(f"Disco {move.disk} movido de {move.source} para {move.target}.")
            except InvalidMoveError as exc:
                print(f"Movimento bloqueado: {exc}")
    except QuitGameError:
        print(f"\nPartida encerrada após {game.move_count} movimento(s). Até a próxima!")
        return

    print("\n" + render_board(game))
    print(
        f"Parabéns! Você resolveu em {game.move_count} movimentos "
        f"(mínimo teórico: {game.expected_min_moves(num_disks)})."
    )


def main() -> None:
    """Ponto de entrada principal da CLI."""
    print("=== Torre de Hanói (CLI) ===")
    num_disks = prompt_int("Quantidade de discos (1 a 8): ", min_value=1, max_value=8)

    print("\nEscolha o modo:")
    print("1 - Resolução automática (recursão)")
    print("2 - Modo manual (jogar)")
    mode = prompt_int("Opção (1 ou 2): ", min_value=1, max_value=2)

    if mode == 1:
        run_automatic_mode(num_disks)
    else:
        run_manual_mode(num_disks)


if __name__ == "__main__":
    main()
