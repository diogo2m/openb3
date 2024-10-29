# Requisitos do Projeto OpenB3

## Requisitos Funcionais

1. **Coleta de Dados:**
   - O sistema deve coletar preços atuais das ações da B3 em tempo real.
   - O DataCollector deve realizar análises de dados, como médias móveis e variações percentuais.

2. **Gerenciamento de Portfólio:**
   - O PortfolioManager deve permitir que os usuários insiram e editem informações sobre seus ativos financeiros.
   - O sistema deve notificar os usuários sobre mudanças relevantes nos seus ativos, como quedas ou aumentos significativos de preço.

3. **Análise de Ações:**
   - O StockAnalyzer deve exibir análises detalhadas de dados financeiros.
   - Deve permitir filtragem das ações com base em critérios como preço, volume, e desempenho histórico.
   - O sistema deve fornecer funcionalidades para cálculos básicos, como lucro/perda, retorno sobre investimento (ROI) e alocação de ativos.

4. **Interface do Usuário:**
   - A interface deve ser intuitiva, permitindo fácil navegação entre as funcionalidades de coleta, gerenciamento e análise.

5. **Notificações:**
   - O sistema deve enviar notificações de alerta via pop-up para manter os usuários informados sobre eventos significativos relacionados aos seus ativos.

## Requisitos Não-Funcionais

1. **Usabilidade:**
   - O sistema deve ser fácil de usar, com uma interface intuitiva que minimize a curva de aprendizado, especialmente para investidores iniciantes.
   - As informações devem estar expostas para o usuário, minimizando informações "escondidadas".

2. **Desempenho:**
   - O sistema deve ser capaz de processar e apresentar dados em tempo real com latência mínima, garantindo que as análises sejam sempre atualizadas.

3. **Compatibilidade:**
   - O software deve ser compatível com os principais sistemas operacionais de desktop (Windows, macOS, e Linux).
   - O sistema deve possibilitar o uso como módulos distintos mas integraveis.

4. **Escalabilidade:**
   - O sistema deve ser projetado para suportar um aumento no volume de dados e no número de usuários sem perda de desempenho.

5. **Documentação e boas práticas:**
   - O código deve ser bem documentado e modular, facilitando a manutenção e a adição de novas funcionalidades no futuro.
   - O sistema deve incluir um sistema de ajuda e suporte ao usuário, incluindo tutoriais e FAQs.
