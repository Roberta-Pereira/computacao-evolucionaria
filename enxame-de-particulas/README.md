<h1 align='center'> Particle Swarm Optimization (PSO)
    
Enxame de partículas </h1> 
    
O algoritmo proposto tem por objetivo encontrar o valor do mínimo global e os pontos em que ele ocorre em funções descontínuas, utilizando técnicas de otimização por meio do algortimo Enxame de Partículas.
PSO é um algoritmo baseado no comportamento social de um bando de pássaros ou enxame de abelhas.

### Informações básicas sobre PSO 
- Um enxame é composto por N partículas que voam pelo espaço de busca D-dimensional;
- Busca a solução ótima dentro de um espaço de busca, através de troca de informações entre as partículas que representam soluções para o problema;
- Todas as partículas têm valores de aptidão que são avaliados pela função de custo para serem otimizadas e têm velocidades que direcionam o vôo das partículas;
- PSO possui uma fácil implementação já que utiliza apenas estruturas primitivas e operadores matemáticos que não possuem grande custo operacional;
- Diferentemente de outros algoritmos evolutivos, o PSO não possui operadores evolutivos como cruzamento e mutação.

### Princípios
O movimento das partículas depende de regras que seguem três fatores:
- Inércia: tendência de se deslocar na direção adotada na iteração anterior;
- Memória: tendência de se deslocar em direção ao melhor ponto encontrado na trajetória individual;
- Cooperação: tendência de se deslocar para o melhor ponto encontrado pelo grupo.

### Funcionamento do algortimo
Cada partícula tem a sua posição e velocidade ajustada a cada iteração, em direção ao ótimo global conforme dois fatores: a melhor posição já visitada por ele e a melhor posição já visitada pelo grupo.

- Atualizar a posição de cada partícula no espaço de decisões;
- Atualizar as melhores posições encontradas até então;
- Atualizar a melhor posição global do grupo.

### Pseudocódigo
![pseudocodigo](https://user-images.githubusercontent.com/50178585/222417462-3012f915-c4c1-4d2b-9f6a-b18b4a342736.PNG)



Para este projeto, o algortimo foi testado nas funções **_peaks_** e **_rastrigin_** fornecidas pelo professor. 
São problemas multimodais, ou seja, possuem vários pontos de máximo e mínimo e o algoritmo deve ser capaz de buscar o mínimo global em cada uma delas. 



