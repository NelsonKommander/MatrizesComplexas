# Calculadora de sistemas lineares

O projeto contido neste repositório tem como objetivo ser uma ferramenta que ajude
no cálculo de sistemas elétricos em anel, resolvendo os sistemas lineares que usam números complexos.

## To Do

- [X] Receber a matriz dos coeficientes e o vetor de termos independentes reais;
- [X] Resolver sistemas lineares reais de qualquer ordem especificada;
- [X] Receber a matriz dos coeficientes e o vetor de termos independentes complexos;
- [X] Resolver sistemas lineares complexos de qualquer ordem especificada;
- [ ] Deixar de receber como entrada a matriz e o vetor, partindo da tabela, montando o sistema linear e resolvendo.


## Instruções de uso

- Instalar o python 3 e a biblioteca numpy (testada na versão 1.20.2);
- Rodar o script e passar o caminho do arquivo de entrada;
- O valor das incógnitas será imprimido na tela.

### Formatação da entrada

As casas decimais dos números devem ser separadas por **'.'** e não por **','**

**O arquivo de entrada deve ter o seguinte formato:**

```
o
c c c ti
c c c ti
c c c ti
```

Onde **'o'** é a ordem da matriz quadrada, **'c'** são os coeficientes e **'ti'** são os termos independentes.

### Trabalhando com números reais


**Exemplo:**

![Sistema linear](https://www.todoestudo.com.br/wp-content/uploads/2020/05/sistema-linear-3.png)

```
2
2 1 5
4 2 10
```

### Trabalhando com números complexos

Os números complexos aparecerão no arquivo de entrada no formato **R|I**, onde
**'R'** é a parte real e **'I'** a parte imaginária.

- A utilização da parte real **'R'** será **obrigatória**!!!; 
- A parte imaginária **'I'**, quando não fornecida será considerada '0j'. 

**Exemplo**

![Matriz Complexa](https://climserv.ipsl.polytechnique.fr/documentation/idl_help/images/Linear_Systems-21.jpg)

```
4
-1 1|-3 2 3|3 15|-2
-2 -1|3 0|1 3|1 -2|-1
3 0|4 0|-1 0|-3 -20|11
2 1|1 2|1 2|1 -10|10  

```