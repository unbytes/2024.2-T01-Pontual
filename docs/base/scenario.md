# 1. Cenário Atual do Cliente e do Negócio

**1.1 Introdução ao Negócio e Contexto**

A CCAA (Centro de Cultura Anglo-Americana) é uma rede de escolas de idiomas fundada no Brasil, focada no ensino de inglês e espanhol. Com uma metodologia própria e interativa, o CCAA busca desenvolver as habilidades de conversação, audição, leitura e escrita dos alunos, utilizando materiais exclusivos e recursos tecnológicos que facilitam a aprendizagem. Presente em várias cidades do Brasil e de outros países, a instituição é conhecida por sua abordagem prática e didática, destinada a estudantes de todas as idades.

Nesse contexto, temos uma filial da CCAA que ao longo do último ano vem enfrentando um crescimento no âmbito empregatício, o qual gerou uma dificuldade e desorganização durante o preenchimento das folhas de ponto dos funcionários. Isso, uma vez que apesar de apresentar uma folha de ponto padrão, o preenchimento é feito manualmente.

Com isso, nota-se que um sistema de software ajudaria a escola a digitalizar o processo sem a necessidade de impressão e com uma significativa redução de erros.

**1.2 Identificação da Oportunidade ou Problema**

Atualmente, na escola, cada funcionário preenche sua própria folha de ponto impressa ao longo do mês, sem um acompanhamento regular da diretoria durante o processo, o que aumenta o risco de erros. Esse método resulta em atrasos na organização dos dados trabalhistas, além de gerar problemas como perdas de registros e esquecimento de marcações devido a erros humanos comuns, comprometendo a precisão das informações. Dessa forma, a escola é prejudicada pela má gestão do preenchimento das folhas de ponto.

Logo, digitalizar o processo de registro do ponto ajudaria a agilizar a marcação de frequência, minimizando os erros de preenchimento e cálculo de horas, além de facilitar o controle da jornada de trabalho pelos superiores. A partir do uso de um recurso digital, as frequências dos funcionários poderão ser armazenadas sem perda de informações, como havia com as folhas, e de modo que todos da diretoria consigam acompanhar o histórico de marcação de ponto dos funcionários.
A figura a seguir representa o diagrama de Ishikawa contendo as causas (6Ms) e o problema da filial da CCAA:

<div align="center" style="background-color: white; border-radius: 25px;">
    <img src="https://raw.githubusercontent.com/mdsreq-fga-unb/2024.2-T01-Pontual/refs/heads/main/docs/assets/ishikawa.png" alt="Diagrama de Ishikawa" width="600" />
</div>

**1.3 Desafios do Projeto**

Dentre as principais dificuldades que envolvem o projeto estão os desafios técnicos relacionados à migração dos últimos dados armazenados no método atual (manual), indicados pelo cliente, para a nova plataforma digital. Isso, visando garantir uma continuidade fluida do processo de marcação do ponto sem a necessidade de uma pausa no negócio. Logo,  será crucial garantir que a transferência ocorra sem perdas de informação, o que requer um planejamento junto a escola para que os dados sejam passados corretamente.

Além disso, os funcionários podem apresentar resistência quanto à digitalização do processo. Essa resistência pode surgir devido a limitações em termos de conhecimento técnico, o que pode dificultar a adaptação ao novo sistema. Para superar essa barreira, será importante desenvolver uma interface com poucos botões na tela, ou seja, no máximo 6 em cada página, ícones, e seções bem definidas de forma que os funcionários consigam entender sozinhos o fluxo de utilização do sistema, além de promover um treinamento básico para apresentar o novo sistema.

Por último, a diversidade de dispositivos móveis utilizados pelos funcionários pode complicar a disponibilidade da aplicação. Esse obstáculo deverá ser cuidadosamente trabalhado pela equipe de desenvolvedores do projeto, garantindo que o sistema funcione em diferentes marcas de celulares e computadores com diversos sistemas operacionais.

**1.4	Segmentação de Clientes**

- **Professores:** Profissionais responsáveis por ensinar e orientar alunos, planejando aulas e avaliações para promover o aprendizado. Além disso, alguns desses profissionais atuam com aulas online.
- **Funcionários Administrativos:** Equipe que gerencia tarefas organizacionais e de suporte ao funcionamento interno, como documentação e atendimento.
- **Funcionários de Suporte:** Profissionais que garantem o funcionamento interno técnico e operacional da instituição, auxiliando nas necessidades diárias.
- **Gestores:** Líderes que planejam, organizam e supervisionam atividades e equipes, assegurando o cumprimento dos objetivos institucionais.
- **Funcionários de manutenção:** Profissionais responsáveis pela manutenção do ambiente de trabalho. Desde a limpeza do ambiente, manuseamento de resíduos e troca de equipamentos defeituosos.

---

## Histórico de Versão

Data       | Versão | Descrição                                                | Autor                      | Revisores
---------- | ------ | -------------------------------------------------------- | -------------------------- | ----------------------------------------
30/10/2024 | 0.1    | Breve descrição inicial do cenário atual e solução proposta | Mateus Vieira, João Lucas, Pedro Gondim | Caio Lamego, Daniela Alarcão
31/10/2024 | 0.2    | Revisão para melhor detalhamento do projeto e adição do Ishikawa  | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão
06/11/2024 | 1.0    | Descrição geral do cenário atual do cliente e do negócio | Mateus Vieira, Caio Lamego | João Lucas, Pedro Gondim, Daniela Alarcão
