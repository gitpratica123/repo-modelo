# Calculadora

Repositório da prática do mini-curso "Coordenando projetos com Git".

Cada trio tem a sua branch `master-grupo-<nome>`: ela faz o papel da `main` do grupo.
Ninguém dá push direto nela; tudo entra por merge request.

| Papel | O que faz |
| --- | --- |
| Dev 1 | cria uma branch, adiciona uma função em `src/soma.py` e abre um MR |
| Dev 2 | faz o mesmo com outra função e resolve o conflito depois do primeiro merge |
| Revisor | lê os MRs no GitLab, comenta e faz o merge |

| Rodada | Dev 1 | Dev 2 |
| --- | --- | --- |
| 1 | `mult` | `div` |
| 2 | `pot` | `resto` |
| 3 | `maior` | `menor` |

A cada rodada, os papéis giram. Os comandos estão nos slides da Parte 6.
