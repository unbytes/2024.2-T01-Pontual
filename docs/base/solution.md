# 2. Solução Proposta

**2.1 Objetivos do Produto**

O objetivo do produto é digitalizar o ponto, modelo o qual otimiza o controle de frequência dos funcionários, facilita o acesso aos dados pela emissão de relatórios mensais e reduz os erros do cálculo de horas. Além disso, permite que as informações sejam armazenadas e acessadas em tempo real pelos diretores e superiores, sem a necessidade de consulta à papelada. Por fim, o produto foca em garantir a consistência da marcação do ponto, permitindo que os diretores e superiores enviem avisos aos funcionários para não esquecerem da marcação.

**2.2 Características da Solução**

- O produto será um sistema focado na utilização mobile, tendo como base principal o estilo PWA (Progressive Web App).
- O registro de ponto deve ser fácil e rápido, ou seja, com o menor número de cliques possível, no máximo 3 para marcação.
- O acesso a partir da página inicial para qualquer outro setor da aplicação deve ter no máximo 6 cliques e/ou ações.
- O sistema deve controlar os atrasos e horas extras de cada funcionário, disponibilizando os cálculos finais e parciais.
- Cada superior pode enviar um lembrete aos seus trabalhadores para marcar o ponto caso o mesmo tenha esquecido.
- Para cada professor que realizar uma aula do tipo VIP o sistema deve notificar os superiores de tal feito.
- Ao final do mês, os relatórios mensais de cada trabalhador podem ser gerados em PDF a partir do template pré definido pela escola.
- Deve haver a opção de assinatura digital do relatório de ponto para cada funcionário, sem a necessidade de impressão.

**2.3 Tecnologias a Serem Utilizadas**

As principais tecnologias que o grupo pretende usar são:

- Flutter
- Python
- Django
- Docker/Docker Compose
- PostgreSQL
- Git/GitHub

**2.4 Pesquisa de Mercado e Análise Competitiva**

No mercado, já existem algumas soluções de registro de ponto. Dentre elas temos o “PontoMais”, “PontoFacil” e “Oitchau”. O “Oitchau”, por exemplo, já oferece uma série de funcionalidades que o nosso cliente busca, como:

- Registro de ponto eletrônico.
- Controle de jornadas de trabalho.
- Relatórios detalhados, ou seja, com cálculo de horas e informações de cada funcionário.

Porém,  a nossa solução se diferencia dessas aplicações nos seguintes pontos:

- **Personalização de regras de negócio:** Ao desenvolver um sistema próprio, podemos personalizar as funcionalidades de acordo com os fluxos de trabalho da escola, incluindo necessidades administrativas específicas. Isso garantirá uma experiência mais alinhada com a realidade da escola.
- **Segurança e Controle de Dados:** A escola terá total controle e privacidade sobre os dados dos funcionários.
- **Custo:** A escola não terá custos financeiros ao adquirir a nossa solução.
- **Facilidade de uso e treinamento:** O sistema desenvolvido de forma personalizada assegura que a interface seja aquela desejada pela escola, permitindo um treinamento rápido dos funcionários.

**2.5 Análise de Viabilidade**

O projeto é viável tecnicamente, visto que a equipe de desenvolvedores já possui experiência prévia nas tecnologias que serão utilizadas. Além disso, o sistema deve contar com dois módulos um de Back-end, que será responsável por gerenciar a API RESTful, e outro de Front-end, que será utilizado para integração entre a aplicação e os funcionários, para os dois módulos, a equipe tem competência para integrar APIs e criar interfaces.

O prazo estimado do projeto é de 3 meses e meio. Isso, já considerando as possíveis modificações de requisitos e implementação no meio do desenvolvimento do sistema.

A equipe demonstra confiança na capacidade de produzir o software, uma vez que ela tem experiência nas áreas de desenvolvimento exigidas. Sendo assim, a viabilidade técnica e de prazo estão ambas dentro das expectativas da escola de inglês.

**2.6 Impacto da Solução**

Com o sistema para digitalizar o processo de marcação de ponto dos funcionários, espera-se que a gestão de ponto da escola tenha os seguintes resultados: 

**Melhoria na gestão de ponto:**
O setor de recursos humanos não necessitará de uma transferência manual das informações em papel para o setor financeiro de gestão dos pagamentos.

**Facilitação do processo para funcionários:**
A digitalização do processo ao invés da utilização de papéis flexibiliza a marcação de ponto, principalmente para os professores que atuam tanto remotamente quanto presencialmente.

**Redução de erros:**
A verificação de horas extras, faltas e atrasos não precisará mais ser feita de forma manual, visto o relatório completo gerado pelo sistema. Além disso, os funcionários não perderão a folha de ponto.

---

## Histórico de Versão

Data       | Versão | Descrição                                                | Autor                      | Revisores
---------- | ------ | -------------------------------------------------------- | -------------------------- | ----------------------------------------
30/10/2024 | 0.1    | Breve descrição inicial do cenário atual e solução proposta | Mateus Vieira, João Lucas, Pedro Gondim | Caio Lamego, Daniela Alarcão
31/10/2024 | 0.2    | Revisão para melhor detalhamento das características do projeto  | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão
06/11/2024 | 1.0    | Descrição geral da solução proposta | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão
