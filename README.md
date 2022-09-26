# GerenciadorCinema

-Como salvar em Json eu "peguei" com meu amigo que está me ajudando neste projeto

Inserimos uma classe de fronteira para representar a interface do sistema e uma classe controladora para interpretar os eventos da interface e solicitar o disparo de métodos nas classes de entidade. A seguir explicaremos as classes de entidade que compõem o diagrama. Nesse diagrama identificamos somente os métodos considerados mais importantes.

1 . Genero
Essa classe armazena os gêneros de filmes apresentados pelo cinema. Seu único atributo é a descrição do gênero do tipo String. **NO**

2. Filme
Essa classe contém o título e a duração de cada filme apresentado no cinema. Seu único método serve para consultar os filmes cadastrados. Observe que um filme está associado a um único gênero, mas um gênero pode estar associado a muitos filmes.**NO**

3. Ator
Essa classe representa os atores que interpretam papéis nos filmes exibidos no cinema. Seu único atributo é o nome do ator.**NO**

4, Atua
Esta é uma classe intermediária entre as classes Ator e Filme e representa os papéis que um ator interpreta em cada filme em que participa. Seu único atributo consiste no papel que um ator interpreta. Observe que um ator pode atuar em no mínimo um e no máximo muitos filmes e que um filme pode ter muitos atores atuando nele, sendo que um filme deve ter, pelo menos, um ator.**NO**

5. Sala
Essa classe armazena as informações sobre as salas pertencentes ao cinema. Seus atributos são número da sala e capacidade da sala, ambos do tipo inteiro. Seu único método permite consultar uma determinada sala e retornar sua capacidade. **falta o editar**

6. Sessão
Essa classe representa as sessões de filmes apresentadas pelo cinema. Seus atributos são data da sessão, hora da sessão, valor do ingresso inteiro, valor do meio ingresso e um atributo para determinar se a sessão já foi encerrada ou não. Observe que uma sessão é apresentada em uma única sala, mas que em uma sala podem ter sido apresentadas muitas sessões. Note também que em uma sessão é exibido somente um filme, mas um filme pode ser exibido em muitas sessões. O único método definido nessa classe permite selecionar as sessões ainda em aberto, retornando uma String com os dados da sessão em questão.**Falta a verificação da sessão, além de verificar o status no BD**

7 , Ingresso
Finalmente, essa classe representa, os ingressos vendidos em cada sessão de cinema. Esta classe armazena o tipo de ingresso, se é um ingresso inteiro ou meio ingresso, tendo ainda um método para gerar um novo ingresso, que retoma verdadeiro (1), se foi possível gerar, ou falso (0), em caso contrário. Uma sessão pode gerar muitos ingressos, contudo, pode não gerar ingresso algum.**NO**
