#  The Food Manager
**Versão 0.1.4** | Lançamento Inicial (CLI)

O **The Food Manager** é um gerenciador de estoques de alimentos desenvolvido para simplificar o controle de inventário. Esta versão inicial estabelece a lógica central do sistema via terminal, priorizando a organização do código e o funcionamento das regras de negócio antes da implementação de interfaces gráficas.

---

### Notas de Atualização (v0.1.4)
> **STATUS: CRUD COMPLETO**
> A atualização 0.1.4 consolidou o sistema CRUD por completo, permitindo agora: **C**criar (Create), **R**ler/Listar (Read), **U** atualizar (Update) e **D**deletar/Remover (Delete). 

*   **Novidade:** Implementada a função de atualização de nome e quantidade de itens com interface de confirmação.
*   **Ciclo de Versões:** Continuaremos com os "packs" de versões **0.1.x** para pequenos ajustes e polimentos antes de partirmos para a grande reestruturação da 0.2.

---

###  O que esperar da Versão 0.2
Como estudante de Engenharia de Computação, entendo que o projeto precisa de uma estrutura mais robusta. A versão 0.2 focará em:
*   **Refatoração para POO:** Migração total das funções para Programação Orientada a Objetos (Classes), facilitando a manutenção e escala.
*   **Performance:** Otimização da estrutura de dados para maior velocidade de resposta.
*   **Nova Estrutura:** Melhoria no design do código e preparação para uma futura UI (User Interface) nas versões 0.2 ou 0.3.

---

### ✅ Funcionalidades Atuais
*   **Cadastro de Itens:** Adicionar novos alimentos com quantidade inicial. `[CONCLUÍDO]`
*   **Remoção:** Excluir registros do estoque permanentemente. `[CONCLUÍDO]`
*   **Ajuste de Saldo:** Funções para aumentar ou diminuir a quantidade de itens. `[CONCLUÍDO]`
*   **Listagem:** Visualização formatada de todos os alimentos e seus respectivos status. `[CONCLUÍDO]`
*   **Update:** Alteração precisa de nomes e quantidades com busca por ID/Nome. `[CONCLUÍDO]`

---

### Desenvolvimento e Estabilidade
Nesta fase, o foco total está na qualidade da lógica de programação.
*   **Interface:** CLI (Command Line Interface).
*   **Persistência:** Manipulação de dados via arquivos JSON.
*   **Manutenção:** Versões incrementais focadas em estabilidade e correções pontuais.

---

### Planejamento Futuro (Roadmap)
- [ ] **Persistência em SQL:** Migração do JSON para banco de dados relacional para maior integridade.
- [ ] **Expansão de Plataforma:** Versões para Web, Desktop e Mobile.
- [ ] **Exportação de Dados:** Geração de relatórios de estoque em formato PDF.
- [ ] **Identificação Visual:** Suporte para imagens dos itens.
- [ ] **Open Source:** Abertura do código para contribuições da comunidade.

---

### 📂 Estrutura de Pastas
```text
food_manager/
│── main.py
│── data/
│   └── initial_data.json
│── modules/
│   ├── add_item.py
│   ├── remove_item.py
│   ├── update_item.py
│   └── list_items.py
│── README.md
```

---
#OpenSource #SoftwareDevelopment #FoodManager #BuildInPublic #Python #DeveloperLife