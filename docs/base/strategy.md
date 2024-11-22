# 3. Estratégias de Engenharia de Software

**3.1 Estratégia Priorizada**

- **Abordagem de Desenvolvimento de Software:** Ágil
- **Ciclo de Vida:** Ágil
- **Processo de Engenharia de Software:** RAD

**3.2 Quadro Comparativo**

| Características                          | RAD (Rapid Application Development)                                                                                                            | ScrumXP                                                                                                                                                     |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Abordagem Geral**                      | Enfatiza o desenvolvimento rápido com prototipação e iterações curtas para atender rapidamente às mudanças nos requisitos do cliente.           | Baseado em metodologias ágeis, combina Scrum (gestão de projetos) com práticas de desenvolvimento do XP (Extreme Programming) para entrega contínua de valor. |
| **Foco em Arquitetura**                  | Arquitetura inicial mínima; foca em desenvolver rapidamente protótipos funcionais para validação.                                                | Evolução contínua da arquitetura, com revisões frequentes e refatorações para manter a qualidade e a simplicidade.                                            |
| **Estrutura de Processos**               | Dividido em quatro fases principais: planejamento de requisitos, design rápido, construção e implementação.                                     | Estruturado em Sprints (Scrum), complementado por práticas técnicas do XP, como programação em pares e TDD.                                                   |
| **Flexibilidade de Requisitos**          | Alta flexibilidade; os requisitos podem mudar frequentemente com base no feedback dos protótipos e usuários.                                    | Os requisitos são priorizados e refinados continuamente, permitindo mudanças rápidas e bem gerenciadas.                                                       |
| **Colaboração com Cliente**              | Envolvimento constante do cliente, que participa ativamente das validações dos protótipos e revisões.                                           | Colaboração próxima e contínua com o cliente ou Product Owner para alinhar expectativas e priorizar entregas.                                                 |
| **Complexidade de Processo**             | Processo simples e flexível, focado em velocidade e adaptação, mas exige coordenação para evitar desorganização.                                | Processo altamente iterativo, mas com regras claras e rituais como planejamento, revisões e retrospectivas.                                                   |
| **Qualidade Técnica**                    | Foco na entrega rápida; a qualidade técnica pode ser sacrificada em favor de prazos curtos.                                                     | Qualidade técnica é prioridade, com práticas como TDD, revisões de código e entrega incremental.                                                              |
| **Práticas de Desenvolvimento**          | Prototipação rápida, desenvolvimento iterativo, e foco em entrega rápida com feedback frequente.                                                | Programação em pares, TDD, integração contínua, refatoração contínua e pequenas entregas frequentes.                                                           |
| **Adaptação à CCAA**                     | Ideal para projetos de curto prazo e baixa complexidade, onde rapidez é mais importante que processos rígidos.                                  | Adequado para equipes de pequeno a médio porte e projetos dinâmicos, com alta prioridade em feedback rápido e entregas contínuas.                             |
| **Documentação**                         | Simples documentação no processo; o foco está no protótipo funcional, mas na fase final há especificação técnica completa                                                      | Documentação mínima, concentrando-se em histórias de usuário e critérios de aceitação escritos no backlog.                                                    |
| **Controle de Qualidade**                | A qualidade é validada principalmente por meio do feedback do cliente em protótipos e entregas rápidas.                                         | Qualidade garantida por práticas de desenvolvimento técnico rigorosas (XP) e revisões regulares.                                                              |
| **Escalabilidade**                       | Limitado a equipes pequenas e projetos simples devido à informalidade e ao foco em entregas rápidas.                                            | Pode escalar com adaptações, mas é mais adequado para projetos ágeis com equipes pequenas a médias.                                                           |
| **Suporte a Equipes de Desenvolvimento** | Suporte limitado para grandes equipes; promove colaboração intensa, mas exige comunicação direta e constante.                                   | Estrutura altamente colaborativa e organizada, promovendo comunicação eficaz e trabalho em equipe.                                                            |

**3.3 Justificativa**

Com base nas características do projeto e nas necessidades discutidas com a cliente, foi escolhida uma abordagem baseada no **RAD (Rapid Application Development)** pelos seguintes motivos:  

- **Prototipação Iterativa para Validação Contínua:**  
  A cliente expressou preferência por validar partes do sistema conforme ele é desenvolvido. O RAD facilita esse processo, entregando protótipos iterativos que podem ser avaliados e ajustados de maneira eficiente sem comprometer os requisitos principais.  

- **Documentação Objetiva:**  
  Apesar do foco na entrega rápida, o projeto exige documentação que registre as mudanças e decisões tomadas durante o desenvolvimento. O RAD foca nos protótipos, portanto, indica exatamente a ideia de documentação mais simples e assertiva, equilibrando a produção com os registros.  

- **Flexibilidade no Cronograma de Comunicação:**  
  Embora o modelo RAD seja iterativo, a comunicação foi definida como flexível, sem a obrigatoriedade de reuniões regulares. Esse alinhamento reforça o foco em ciclos rápidos de desenvolvimento com entregas intermediárias úteis para avaliação.  

- **Simplicidade no Controle de Qualidade:**  
  O modelo RAD prioriza o feedback do cliente em relação aos protótipos, garantindo que as entregas estejam alinhadas às expectativas sem introduzir processos complexos de validação.  

**Observação:** O RAD tem a ideia dos requisitos variáveis de acordo com os feedbacks do cliente. Entretanto, para esse projeto vamos modificar essa característica, pois a cliente já tem uma ideia bem definida do que deseja. Portanto, os requisitos serão fixos e não sofrerão alterações durante o desenvolvimento.

---

## 📚 Referências

- **Team Kissflow (2024). What is Rapid Application Development (RAD)? An Ultimate Guide for 2024.** <a href="https://kissflow.com/application-development/rad/rapid-application-development/">Link</a>. Acesso em: 22 de novembro de 2024.

- **Johan Paul (2008). Quantitative Approach for Lightweight Agile Process Assessment.** Acesso em: 6 de novembro de 2024.

## Histórico de Versão

Data       | Versão | Descrição                                                              | Autor                      | Revisores                                 |
---------- | ------ | ---------------------------------------------------------------------- | -------------------------- | ----------------------------------------- |
06/11/2024 | 0.1    | Definição da abordagem, ciclo e processo junto ao quadro comparativo   | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão |
09/11/2024 | 0.2    | Finalização da justificativa para o processo de Engenharia de Software | Mateus Vieira, João Lucas, Pedro Gondim | Caio Lamego, Daniela Alarcão |
14/11/2024 | 0.3    | Referências | Daniela Alarcão | |
22/11/2024 | 1.0    | Revisão da escolha de processo e concretização | Mateus Vieira | Caio Lamego |
