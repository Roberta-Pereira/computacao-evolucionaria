<h1 align='center'> Algortimo Evolução Diferencial
    
DE/rand/1/bin </h1> 
    
O algoritmo proposto tem por objetivo encontrar o valor do mínimo global e os pontos em que ele ocorre, em funções descontínuas utilizando técnicas de otimização por meio de um algortimo de evolução diferencial. 
    
### Conceitos Básicos
* População: Uma população é constituída de N indivíduos. Cada indivíduo corresponde a uma solução candidata e é representado por um vetor coluna com as variáveis de decisão do problema.
* Mutação: É o mecanismo de busca do algortimo, por meio de vetores-diferença. Dois indivíduos são escolhidos aleatoriamente para criar um vetor diferença, aplicando-se um fator de escala. Este vetor é somado a um terceiro indivíduo escolhido aleatoriamente, chamado de vetor de base, formando uma solução mutante.
* Recombinação: Indivíduos da população corrente são recombinados com a população mutante produzindo uma população de soluções teste U. A recombinação ocorre com uma probabilidade C de maneira a controlar seu efeito e para a variável de decisao escolhida através do indice delta gerado aleatoriamente.
* Seleção: Visa escolher, dentre a população corrente e a população cruzada, os indivíduos para a próxima geração.

**Notação: DE/base/d/rec**
* DE -> algoritmo
* base -> base indica a forma como o vetor de base é selecionado
* d -> indica o número de vetores diferença
* rec -> faz referência ao operador de recombinação utilizado
</p>
    
Para o problema proposto foi utilizada a versão clássica do algortimo: **DE/rand/1/bin**
<ol type="i">
<li> Seleção aleatória do vetor base com probabilidade uniforme; </li>
<li> Um (01) vetor-diferença para a mutação; </li>
<li> Recombinação discreta entre a solução corrente e seu vetor mutante correspondente. </li>
</ol>

Para este projeto, o algortimo foi testado nas funções **_peaks_** e **_rastrigin_** fornecidas pelo professor. 
São problemas multimodais, ou seja, possuem vários pontos de máximo e mínimo e o algoritmo deve ser capaz de buscar o mínimo global em cada uma delas. 
