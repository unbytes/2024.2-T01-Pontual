# 3. Estratégias de Engenharia de Software

**3.1 Estratégia Priorizada**

- **Abordagem de Desenvolvimento de Software:** Híbrida
- **Ciclo de Vida:** Iterativo
- **Processo de Engenharia de Software:** Spiral

**3.2 Quadro Comparativo**

| Características                          | Spiral                                                                                                                                          | Processo Unificado                                                                                                                                               |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Abordagem Geral**                      | Iterativo e baseado em ciclos de prototipação e análise de risco.                                                                               | Iterativo, incremental com entregas constantes e revisões frequentes                                                                                             |
| **Foco em Arquitetura**                  | Forte ênfase na identificação e mitigação de riscos arquiteturais logo no início dos ciclos, visando continuar ou interromper a construção.     | Destaque na definição de uma arquitetura sólida durante as fases iniciais, orientando todo o desenvolvimento.                                                    |
| **Estrutura de Processos**               | Organizado em ciclos ou espirais, com fases de planejamento, análise de riscos, engenharia e avaliação.                                         | Dividido em quatro fases (Concepção, Elaboração, Construção, Transição), cada uma com atividades específicas e incrementais                                      |
| **Flexibilidade de Requisitos**          | Os requisitos são tratados como fixos para cada ciclo de desenvolvimento.                                                                       | Permite ajustes nos requisitos a cada iteração, incorporando feedback contínuo.                                                                                  |
| **Colaboração com Cliente**              | Colaboração frequente com o cliente para revisão dos protótipos e definição de novas direções.                                                  | Interação contínua com clientes e usuários, especialmente nas fases de Concepção e Transição.                                                                    |
| **Complexidade de Processo**             | Processo formal e complexo devido à análise de riscos e prototipação em cada iteração.                                                          | Processo estruturado e formal, exigindo conhecimento detalhado das fases e fluxos de trabalho.                                                                   |
| **Qualidade Técnica**                    | A qualidade técnica é garantida a cada ciclo por meio da análise de riscos e validação da arquitetura e funcionalidades.                        | Cada iteração produz um sistema funcional e testado, garantindo uma qualidade próxima ao produto final.                                                          |
| **Práticas de Desenvolvimento**          | Uso de prototipação e análise de riscos para guiar o desenvolvimento, com foco menor em práticas ágeis e maior em validação incremental.        | Utiliza casos de uso e UML para modelagem, estruturando requisitos e implementações claramente, além de testes rigorosos para garantir a qualidade do produto.   |
| **Adaptação à CCAA**                     | Ideal para projetos complexos de longo prazo que exigem mitigação de riscos e maior feedback dos clientes. Pode ser adaptado para menor escala. | Ideal para projetos que exigem uma arquitetura bem estruturada desde o começo, com ciclos iterativos e incrementais, permitindo ajustes e melhorias contínuas.   |
| **Documentação**                         | Exige documentação clara e detalhada para cada fase e protótipo, incluindo plano de risco, justificativas e soluções.                           | Documentação detalhada, especialmente durante a Análise e Projeto, para suporte a equipes.                                                                       |
| **Controle de Qualidade**                | Controle íntegro a partir da análise de risco em cada iteração do processo.                                                                     | Inclui testes rigorosos em cada iteração e monitoramento contínuo dos riscos, identificados e mitigados nas fases iniciais.                                      |
| **Escalabilidade**                       | Adequado para projetos grandes em que a mitigação de riscos é crucial.                                                                          | A estrutura modular permite que o sistema cresça com novas funcionalidades em ciclos futuros.                                                                    |
| **Suporte a Equipes de Desenvolvimento** | Suporte para equipes maiores e estruturadas com papéis bem definidos, com controle maior sobre os ciclos.                                       | Suporta equipes maiores com papéis bem definidos, exigindo controle detalhado sobre o progresso em cada fase do projeto, promovendo organização e eficiência.    |

**3.3 Justificativa**

Com base nas características do projeto e nas necessidades discutidas com a cliente, foi escolhida uma abordagem híbrida para o desenvolvimento pelos seguintes motivos:

- **Definição Fixa dos Requisitos e Documentação Assertiva:**
Após conversa com a cliente, ficou claro que todos os requisitos devem ser definidos como fixos desde o início. Há também a necessidade de uma documentação precisa das modificações realizadas ao longo do desenvolvimento, para que possam ser mapeadas entre as reuniões.

- **Flexibilidade no Modelo de Comunicação e Feedbacks:**
O modelo de comunicação entre a equipe e a cliente foi definido como flexível, sem a obrigatoriedade de reuniões pré-datadas ou um plano de entregas fixo. Em vez disso, será feito um acompanhamento contínuo das mudanças até a entrega final e única da aplicação.

- **Ciclo de Vida Iterativo:**
Ao longo do projeto, decidiu-se que o ciclo de vida mais adequado para o desenvolvimento é o Iterativo, permitindo revisões e feedbacks em partes do projeto. Essa abordagem possibilita adaptações graduais, garantindo flexibilidade para alterações ao longo do trabalho e culminando em uma única entrega ao final.

- **Seleção do Modelo Spiral:**
Considerando a maior parte das características do projeto, foi selecionado o modelo Spiral. Esta escolha se justifica pelos requisitos fixos e pelo foco na produção de protótipos, que serão aprimorados com base nos feedbacks da cliente. Esse modelo permite que cada etapa seja executada com segurança, minimizando os riscos de interrupção.

---

## 📚 Referências

- **Eternal Sunshine Of The Mind (2013). The Spiral Model.** <a href="https://eternalsunshineoftheismind.wordpress.com/2013/03/06/the-spiral-model-4/">Link</a>. <br>Acesso em: 6 de novembro de 2024.

- **Johan Paul (2008). Quantitative Approach for Lightweight Agile Process Assessment.** <br>Acesso em: 6 de novembro de 2024.

## Histórico de Versão

Data       | Versão | Descrição                                                              | Autor                      | Revisores
---------- | ------ | ---------------------------------------------------------------------- | -------------------------- | ----------------------------------------
06/11/2024 | 0.1    | Definição da abordagem, ciclo e processo junto ao quadro comparativo   | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão
09/11/2024 | 0.2    | Finalização da justificativa para o processo de Engenharia de Software | Mateus Vieira, João Lucas, Pedro Gondim | Caio Lamego, Daniela Alarcão
14/11/2024 | 0.3    | Referências | Daniela Alarcão | 
