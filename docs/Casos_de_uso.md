## Caso de uso 1: Adicionar um ativo na carteira
**Ator:** Usuário  
**Descrição:** Esse caso de uso descreve como o usuário adiciona um ativo na carteira. O ativo pode ser qualquer ativo presente na B3.

### Condições prévias
1. O usuário deve estar credenciado no sistema.
2. O sistema deve estar conectado à internet para acessar dados em tempo real.

### Caminho normal
1. O usuário navega até a seção de gerenciamento de portfólio.
2. O usuário seleciona a opção "Adicionar ativo".
3. O sistema solicita que o usuário insira o código do ativo (ex: PETR4).
4. O usuário fornece os detalhes da transação, como quantidade e preço de compra.
5. O sistema valida as informações e confirma a adição do ativo à carteira.
6. O sistema atualiza a lista de ativos do usuário e recalcula os valores totais.

### Condições posteriores
1. O ativo é adicionado ao portfólio do usuário com as informações fornecidas.

### Input/Output
| Entradas           | Fonte       | Saídas                   | Destino               |
| ------------------ | ----------- | ------------------------ | --------------------- |
| Código do ativo    | Usuário     | Confirmação de sucesso   | Interface do usuário  |
| Quantidade         | Usuário     | Atualização da carteira  | Banco de dados        |
| Preço de compra    | Usuário     | Recalcula valores totais | Banco de dados        |

---


## Caso de uso 2: Ativar monitoramento de ativo
**Ator:** Usuário  
**Descrição:** Esse caso de uso descreve como o usuário ativa o monitoramento de preço de um ativo específico.

### Condições prévias
1. O usuário deve estar credenciado no sistema.
2. O ativo já deve estar adicionado na carteira do usuário.

### Caminho normal
1. O usuário acessa a seção de monitoramento de ativos.
2. O usuário seleciona um ativo que já está na carteira.
3. O sistema solicita que o usuário defina os limites de alerta para o preço do ativo.
4. O sistema ativa o monitoramento e confirma a configuração.

### Condições posteriores
1. O sistema começa a monitorar o ativo de acordo com os limites definidos.
2. O usuário é notificado quando o preço do ativo atinge os valores estabelecidos.

### Input/Output
| Entradas           | Fonte       | Saídas                       | Destino               |
| ------------------ | ----------- | ---------------------------- | --------------------- |
| Limite superior    | Usuário     | Confirmação de monitoramento | Interface do usuário  |
| Limite inferior    | Usuário     | Notificação de alertas       | Banco de dados        |

---


## Caso de uso 3: Pesquisar ativos por índices
**Ator:** Usuário  
**Descrição:** Esse caso de uso descreve como o usuário pesquisa ativos na B3 com base em índices financeiros.

### Condições prévias
1. O usuário deve estar credenciado no sistema.
2. O sistema deve ter acesso aos dados financeiros atualizados dos ativos.

### Caminho normal
1. O usuário acessa a seção de pesquisa de ativos.
2. O usuário seleciona os critérios de busca (ex: P/E Ratio, Dividend Yield).
3. O sistema processa a solicitação e filtra os ativos com base nos critérios especificados.
4. O sistema exibe a lista de ativos que correspondem aos filtros.

### Condições posteriores
1. A lista de ativos filtrados é apresentada ao usuário.
2. O usuário pode adicionar qualquer um desses ativos à sua carteira ou monitorá-los.

### Input/Output
| Entradas             | Fonte       | Saídas                  | Destino               |
| -------------------- | ----------- | ----------------------- | --------------------- |
| Critérios de filtro  | Usuário     | Lista de ativos         | Interface do usuário  |
| Valor dos índices    | Sistema     | Dados atualizados       | Interface do usuário  |
