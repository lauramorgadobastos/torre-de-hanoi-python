# Documentação Técnica

Este diretório contém o núcleo da aplicação, separado entre regra de negócio/algoritmo e interface de linha de comando.

## Arquivos

### `src/hanoi.py`
Contém a lógica independente de interface:
- `Move`: *dataclass* imutável (`frozen=True`) que representa um movimento (`disk`, `source`, `target`).
- `InvalidMoveError`: exceção especializada (`ValueError`) lançada quando um movimento viola as regras do jogo ou usa pinos inválidos.
- `HanoiGame`: gerencia o estado dos pinos (`A`, `B`, `C`), o histórico de movimentos (`history`), a validação (`can_move`, `move_disk`), a verificação de vitória (`is_solved`) e o cálculo do mínimo teórico de movimentos (`expected_min_moves`).
- `solve_hanoi_recursive`: função recursiva que retorna a lista de `Move` para resolver o problema de `num_disks` discos.

### `src/main.py`
Responsável pela interação no terminal e apresentação visual:
- `prompt_int` e `prompt_rod`: leitura e validação de entradas do usuário (incluindo comandos de saída no modo manual via `QuitGameError`).
- `render_board`: monta a representação visual dos pinos e discos em modo texto.
- `run_automatic_mode` e `run_manual_mode`: conduzem os dois modos de execução utilizando `HanoiGame` e `solve_hanoi_recursive`.
- `main`: ponto de entrada da CLI.