# PyStock

<p align="center">
  <img src="./assets/Pystock-icon.png" width="500" alt="AXON Automotive Manager Logo"/>
</p>


[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version 0.1.4](https://img.shields.io/badge/version-0.1.4-brightgreen)]()
[![Status: Active](https://img.shields.io/badge/status-active-success)]()

**PyStock** é um sistema robusto de gerenciamento de estoque de alimentos desenvolvido em Python. Oferece uma solução prática via CLI (Command Line Interface) para controlar inventário com funcionalidades completas de CRUD, interface intuitiva e persistência de dados em JSON.

## Visão Geral

O PyStock foi desenvolvido para simplificar o controle de inventário de alimentos, permitindo que usuários gerenciem seu estoque de forma eficiente através de um terminal. Com uma arquitetura modular e funcionalidades bem definidas, o projeto estabelece a lógica central para futuras expansões em versões posteriores.

**Status:** CRUD Completo | **Versão Atual:** 0.1.4 | **Foco:** Estabilidade & Qualidade

---

## Começando Rápido

### Pré-requisitos
- Python 3.8 ou superior
- Sistema operacional: Windows, macOS ou Linux

### Instalação

```bash
# Clone o repositório
git clone https://github.com/luke-lynx/pystock.git
cd pystock

# Nenhuma dependência externa necessária
# O projeto utiliza apenas bibliotecas padrão do Python
```

### Primeiro Uso

```bash
# Na raiz do projeto, execute:
python src/main.py

# Siga as instruções:
# 1. Confirme a criação do arquivo de dados
# 2. Escolha se deseja adicionar 50 itens padrão
# 3. Use o menu principal para gerenciar seu estoque
```

---

## Funcionalidades

| Funcionalidade | Status | Descrição |
|---|---|---|
| Cadastro de Itens | ✓ Concluído | Adicionar novos alimentos com quantidade inicial |
| Listagem de Estoque | ✓ Concluído | Visualizar todos os itens com status (OK, BAIXO, ESGOTADO) |
| Remoção de Itens | ✓ Concluído | Deletar registros permanentemente do estoque |
| Atualização de Dados | ✓ Concluído | Alterar nome e quantidade com busca por ID ou Nome |
| Interface CLI | ✓ Concluído | Menu intuitivo e responsivo |

---

## Guia de Uso

### 1. Adicionar Item

```
Menu Principal → Opção 1 (Adicionar Alimento)
├─ Digite o nome do alimento
├─ Digite a quantidade inicial
└─ Confirme os dados
```

**Funcionalidades:**
- Validação de entrada (quantidade deve ser número não-negativo)
- Confirmação antes de adicionar
- Geração automática de ID
- Persistência imediata em JSON

### 2. Listar Estoque

```
Menu Principal → Opção 4 (Listar Estoque)
```

**Informações Exibidas:**
- ID do item
- Nome do alimento
- Quantidade em estoque
- Categoria (padrão: "Geral")
- Status:
  - **OK**: Quantidade > 5 unidades
  - **BAIXO**: Quantidade entre 1-5 unidades
  - **ESGOTADO**: Quantidade = 0

### 3. Remover Item

```
Menu Principal → Opção 2 (Remover Alimento)
├─ Escolha: buscar por ID ou Nome
├─ Confirme o item encontrado
└─ Confirme a remoção
```

### 4. Atualizar Item

```
Menu Principal → Opção 3 (Alterar Alimento)
├─ Busque pelo ID
├─ Altere nome e/ou quantidade
├─ Revise as mudanças
└─ Confirme e grave
```

---

## Arquitetura

### Estrutura de Diretórios

```
pystock/
├── src/
│   ├── main.py                 # Ponto de entrada
│   └── modules/
│       ├── add_item.py         # Funcionalidade de criar
│       ├── list_item.py        # Funcionalidade de listar
│       ├── remove_item.py      # Funcionalidade de deletar
│       └── update_item.py      # Funcionalidade de atualizar
├── data/
│   ├── user_data.json          # Banco de dados do usuário
│   └── initial_data.json       # Dados padrão (50 itens)
├── .gitignore
└── README.md
```

### Modelo de Dados

Cada item no estoque segue a seguinte estrutura JSON:

```json
{
  "id": 1,
  "nome": "Arroz 5kg",
  "quantidade": 100,
  "categoria": "Grãos"
}
```

**Campos:**
- `id` (int): Identificador único, gerado automaticamente
- `nome` (string): Nome do alimento
- `quantidade` (int): Quantidade em estoque (≥ 0)
- `categoria` (string): Classificação do item (extensível para futuras versões)

### Fluxo de Dados

```
CLI Input → Validação → Processamento → JSON File → CLI Output
                              ↓
                       Persistência
```

---

## Versões e Roadmap

### v0.1.x Series - Consolidação
**Foco:** Estabilidade da lógica core e refinamento da interface CLI

- v0.1.4 (Atual) - CRUD Completo
- v0.1.5 - Melhorias UI/UX e tratamento de erros
- v0.1.6+ - Pequenos ajustes baseados em feedback

### v0.2.0 - Refatoração Arquitetural
**Foco:** Migração para POO (Programação Orientada a Objetos)

- [ ] Implementar classes: `Inventory`, `Item`, `FileManager`
- [ ] Padrão de design: Repository Pattern
- [ ] Melhorar performance e escalabilidade
- [ ] Adicionar logging e debugging

### v0.3.0+ - Expansão de Plataforma

- [ ] API REST (FastAPI/Flask)
- [ ] Banco de dados SQL (PostgreSQL/SQLite)
- [ ] Interface Web (React/Vue)
- [ ] Aplicativo Desktop (Tkinter/PyQt)
- [ ] Relatórios em PDF
- [ ] Suporte a imagens de produtos

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|---|---|---|
| Python | 3.8+ | Linguagem principal |
| JSON | - | Persistência de dados |
| Pathlib | - | Gerenciamento de caminhos |
| OS | - | Limpeza de terminal |

**Bibliotecas Utilizadas:**
- `pathlib` - Manipulação de caminhos (multiplataforma)
- `json` - Serialização/desserialização de dados
- `os` - Operações do sistema operacional
- `time` - Controle de tempo em transições

---

## Contribuição

Contribuições são bem-vindas! Este projeto está em desenvolvimento ativo.

### Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Padrões de Código

- Seguir PEP 8 (Python Enhancement Proposal 8)
- Usar nomes descritivos para variáveis e funções
- Adicionar comentários em lógicas complexas
- Testar funcionalidades antes de commitar

### Reportar Bugs

Encontrou um bug? Abra uma [issue](https://github.com/luke-lynx/pystock/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. observado
- Versão do Python e SO utilizado

---

## Validação e Segurança

### Validações Implementadas

| Campo | Validação |
|---|---|
| Nome do Item | Não vazio, string |
| Quantidade | Inteiro não-negativo (≥ 0) |
| ID | Gerado automaticamente, único |
| Confirmação | Aceita: s, sim, y, yes (case-insensitive) |

### Considerações de Segurança

- Arquivo JSON é sobrescrito atomicamente em operações de escrita
- Validação de entrada em todos os pontos de interface
- Tratamento de exceções em operações críticas
- Encoding UTF-8 para suporte a caracteres especiais

---

## Troubleshooting

### Problema: "Arquivo user_data.json não encontrado"
**Solução:** Execute o programa novamente e confirme a criação do arquivo na inicialização.

### Problema: "Invalid Value: Please Type Again"
**Solução:** Verifique se a quantidade inserida é um número inteiro não-negativo.

### Problema: Item não encontrado ao atualizar
**Solução:** Consulte a listagem (Opção 4) para confirmar o ID correto do item.

### Problema: Programa não executa no Windows/Mac
**Solução:** Certifique-se de ter Python 3.8+ instalado e use `python` ou `python3` conforme sua configuração.

---

## Roadmap Visual

```
v0.1.4 (Atual)
    ↓ (Pequenos ajustes)
v0.1.5 → v0.1.6 → v0.1.x
    ↓ (Refatoração completa)
v0.2.0 (POO + Performance)
    ↓ (Expansão)
v0.3.0+ (Multi-plataforma + API)
```

---

## Créditos

Desenvolvido por **@luke-lynx** como projeto de aprendizado em Engenharia de Computação.

Este projeto demonstra:
- Lógica de programação sólida
- Gestão de arquivos e persistência de dados
- Design de interface CLI intuitiva
- Estrutura modular e escalável

---

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

---

## Contato & Suporte

- GitHub: [@luke-lynx](https://github.com/luke-lynx)
- Issues: [Abra uma discussão](https://github.com/luke-lynx/pystock/issues)
- Discussões: [GitHub Discussions](https://github.com/luke-lynx/pystock/discussions)

---

**PyStock** - Sistema inteligente de gerenciamento de estoque. Desenvolvido com ❤️ em Python.
