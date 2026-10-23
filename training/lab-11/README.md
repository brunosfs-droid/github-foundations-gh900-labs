# LAB 11 — GitHub Copilot: gerar, revisar e testar

## Pré-requisitos
- Acesso ao GitHub Copilot em um editor compatível ou no GitHub (conforme seu plano).
- Conferir `.github/copilot-instructions.md`.
- Trabalhar somente na branch `lab-11/copilot-tests`; PR ainda em Draft.

## Etapa 1 — Ler o código existente
Abra `training/lab-10/calculator.py` e `training/lab-10/test_calculator.py`. Identifique os três testes já existentes.

## Etapa 2 — Prompt para o Copilot
> Analise `training/lab-10/calculator.py` e os testes existentes. Proponha testes adicionais em `unittest` para entradas negativas, resultados decimais, zero como numerador e propriedades básicas de soma. Preserve as assinaturas de `add` e `divide`, não acrescente bibliotecas externas e não altere workflows. Explique os casos de borda e mostre o diff esperado antes de aplicar.

## Etapa 3 — Revisão humana
- Verificar se cada teste realmente exercita o cenário descrito.
- Rejeitar sugestões duplicadas, incorretas ou que alterem o escopo.
- Adicionar apenas testes úteis em `training/lab-10/test_calculator.py` na branch do LAB 11.
- Conferir `Files changed`; documentar se o Copilot respeitou as instruções e onde precisou de correção.

## Etapa 4 — Validação
Executar localmente: `python -m unittest discover -s training/lab-10 -p 'test_*.py' -v`.
A PR contra main também deve acionar o workflow `LAB 10 - Python CI`; inspecionar a execução e seu resultado.

## Evidências para o checkpoint
Informe o prompt utilizado, número total de testes, casos adicionados, resultado do CI e um exemplo de sugestão aceita, corrigida ou rejeitada. Não publicar informações sensíveis.

## Critério de liberação
Manter a PR Draft e não executar merge até validação explícita.
