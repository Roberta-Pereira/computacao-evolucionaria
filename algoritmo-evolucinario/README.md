<h1 align='center'> Algoritmo Evolucionário:
  
 N-rainhas </h1>

<p align="center"> “Dado um tabuleiro de xadrez regular (NxN) e N rainhas, posicione as N Rainhas no tabuleiro de forma que elas não se coloquem em xeque” </p>

O algoritmo proposto tem por objetivo utilizar a abordagem de Computação Evolucionária para obter a melhor distribuição das N rainhas 
em um tabuleiro com o menor número de conflitos possíveis. 
Os conflitos ocorrem quando duas rainhas se encontram na mesma linha ou coluna.

<h3> Caracteristicas da solução </h3>
<table>
  <tr>
    <td> Representação da população </td>
    <td> Permutação de N inteiros </td>
  </tr>
  <tr>
    <td> Operador de Recombinação </td>
    <td> Cut and Crossfill </td>
  </tr>
  <tr>
    <td> Operador de Mutação </td>
    <td> Swap Mutation </td>
  </tr>
  <tr>
    <td> Seleção dos Pais </td>
    <td> Torneio </td>
  </tr>
  <tr>
    <td> Seleção dos Sobreviventes </td>
    <td> Geracional </td>
  </tr>
</table>

<h3> Pseudocódigo para solução do problema: </h3>

![Pseudocodigo](https://user-images.githubusercontent.com/50178585/214324666-61b21447-366b-4a6e-9c88-4eeb4dec64cf.PNG)

Nota: Como a maior parte do processo é aleatória, nem sempre leva o mesmo tempo para convergir para uma solução.
