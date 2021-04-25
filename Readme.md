# Calculadora de sistemas lineares

O projeto contido neste repositório tem como objetivo ser uma ferramenta que ajude
no cálculo de sistemas elétricos em anel, resolvendo os sistemas lineares que usam números complexos.

## To Do

- [X] Receber a matriz dos coeficientes e o vetor de termos independentes reais
- [X] Resolver sistemas lineares reais de qualquer ordem especificada
- [ ] Receber a matriz dos coeficientes e o vetor de termos independentes complexos
- [ ] Resolver sistemas lineares complexos de qualquer ordem especificada
- [ ] Deixar de receber como entrada a matriz e o vetor, partindo da tabela, montando o sistema linear e resolvendo


## Instruções de uso

- Instalar o python 3 e a biblioteca numpy (testada na versão 1.20.2)
- Rodar o script e passar o caminho do arquivo de entrada
- O valor das incógnitas será imprimido na tela

### Trabalhando com números reais

As casas decimais dos números devem ser separads por '.' e não por ','

**O arquivo de entrada deve ter o seguinte formato:**

```
o
c c c ti
c c c ti
c c c ti
```

Onde **'o'** é a ordem da matriz, **'c'** são os coeficientes e **'ti'** são os termos independentes


**Exemplo:**

![Sistema linear](https://www.todoestudo.com.br/wp-content/uploads/2020/05/sistema-linear-3.png)

```
2
2 1 5
4 2 10
```

### Trabalhando com números complexos

**WIP**

Os números complexos aparecerão no arquivo de entrada no formato **R|I**, onde
**'R'** é a parte real e **'I'** a parte imaginária
