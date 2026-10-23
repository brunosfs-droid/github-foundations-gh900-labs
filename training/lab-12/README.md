# LAB 12 — github.dev, Codespaces e Dev Containers

## Objetivo
Comparar editor web, ambiente remoto interativo e especificação de ambiente. Não provisionar recursos de nuvem automaticamente.

## A. github.dev — custo zero
1. Na branch `lab-12/devcontainers-codespaces`, abra o repositório pelo botão `.` ou `github.dev`.
2. Inspecione `.devcontainer/devcontainer.json` e este README. Observe que o editor web não fornece um terminal de execução.
3. Registre o que pode e não pode fazer no github.dev.

## B. Codespaces — opcional, sujeito à cota
1. Consulte sua cota e configurações de cobrança antes de criar um Codespace.
2. Se houver cota disponível e limites adequados, selecione a branch do LAB 12 e a menor máquina apropriada.
3. Aguarde a criação do ambiente. No terminal, execute:

```bash
python --version
python -m unittest discover -s training/lab-10 -p 'test_*.py' -v
```

4. Espere **7 testes** aprovados, caso os testes anteriores não tenham sido modificados.
5. Pare o Codespace após a prática. Exclua-o quando não precisar manter seu armazenamento.
6. Se não houver cota, não crie recursos pagos: documente a limitação e utilize o resultado do GitHub Actions na PR.

## C. GitHub Actions
Inspecione o workflow `LAB 10 - Python CI` disparado por `pull_request` para `main`; compare os jobs automatizados com o terminal interativo de Codespaces.

## Evidências do checkpoint
- Qual branch foi utilizada?
- Qual diferença observou entre github.dev e Codespaces?
- Criou Codespace? Se sim, qual a versão Python e quantos testes passaram? Se não, por quê?
- Qual é o resultado dos checks desta PR?

## Política de merge
Manter a PR Draft até revisão e autorização expressa do aluno.
