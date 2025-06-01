# 📝 Relatório Técnico da Aplicação de Cadastro de Clientes e Contratos

## 1. Objetivo da Aplicação
A aplicação foi desenvolvida para realizar o gerenciamento de **clientes e seus contratos comerciais**. Seu objetivo principal é permitir o **cadastro, listagem e associação de contratos a clientes**, utilizando um banco de dados PostgreSQL remoto.

---

## 2. Tecnologias Utilizadas
- **Linguagem**: Python 3.x  
- **Banco de Dados**: PostgreSQL (Render.com)  
- **Bibliotecas**:
  - `psycopg2`: Conexão com PostgreSQL
  - `datetime`: Manipulação de datas (reserva para uso futuro)
- **Interface**: Terminal (CLI - Command Line Interface)

---

## 3. Funcionalidades
- **Cadastro de Clientes**  
  Armazena nome e CPF do cliente.

- **Cadastro de Contratos**  
  Armazena número, valor, data de assinatura e ID do cliente.

- **Listagem de Contratos por Cliente**  
  Permite consultar todos os contratos vinculados a um cliente específico.

- **Exibição Geral**  
  Exibe todos os clientes e contratos registrados.

- **Menu Interativo**  
  Navegação por opções numeradas no terminal.

---

## 4. Estrutura do Banco de Dados

### Tabela `clientes`
| Campo     | Tipo   | Observação            |
|-----------|--------|------------------------|
| idCliente | SERIAL | Chave primária         |
| nome      | TEXT   | Nome completo           |
| cpf       | TEXT   | CPF (sem validação)     |

### Tabela `contratos`
| Campo          | Tipo     | Observação                            |
|----------------|----------|----------------------------------------|
| idContrato     | SERIAL   | Chave primária                        |
| numero         | TEXT     | Identificador do contrato             |
| valor          | REAL     | Valor financeiro do contrato         |
| dataAssinatura | DATE     | Data da assinatura do contrato        |
| idCliente      | INTEGER  | Chave estrangeira para `clientes`     |

---

## 5. Fluxo de Execução
1. Inicia com `init_db()` para garantir tabelas criadas.
2. Exibe menu com as opções:
   - Cadastrar cliente
   - Cadastrar contrato
   - Listar contratos de um cliente
   - Exibir todos os dados
   - Sair
3. Usuário interage via terminal inserindo dados.

---

## 6. Boas Práticas e Validações
- Uso de `IF NOT EXISTS` na criação de tabelas.
- Verificação da existência do cliente antes de inserir contratos.
- Uso de classes `Cliente` e `Contrato` para organização da lógica.

---

## 7. Melhorias Futuras Sugeridas
- ✅ Validação de CPF (formato e duplicidade)
- ✅ Tratamento de exceções (`try-except`)
- ✅ Autenticação de usuários
- ✅ Exportação de dados (PDF, CSV)
- ✅ Testes unitários com `pytest`
- ✅ Filtros e paginação em listagens

---

## 8. Conclusão
A aplicação cumpre seu objetivo principal com simplicidade e eficácia. Tem base sólida para escalar, seja com uma interface web, exportação de dados ou relatórios interativos.

---
Optativa: Programação básica Python para Direito
Prof. Julio Arakaki
Avaliação2 29/05/2025

