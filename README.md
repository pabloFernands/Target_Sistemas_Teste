# Target_Sistemas_Teste

## 1) Observe o trecho de código:

int INDICE = 12, SOMA = 0, K = 1;

enquanto K < INDICE faça

{ K = K + 1; SOMA = SOMA + K;}

imprimir(SOMA);

**Resposta: SOMA = 78**


## 2) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, _**9**_
**valor x + 2**

b) 2, 4, 8, 16, 32, 64, __**128**__
**Dobro do valor x**

c) 0, 1, 4, 9, 16, 25, 36, __**49**__
**É o quadrado dos numeros 0, 1, 2, 3, 4, 5, 6 **

d) 4, 16, 36, 64, __**100**__
**É o quadrado dos numeros pares 2, 4, 6, 8, 10**

e) 1, 1, 2, 3, 5, 8, __**13**__
**Soma dos dois numeros anteriores**

f) 2,10, 12, 16, 17, 18, 19, ____
**Não entendi.**

## 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora de todos os dias de um ano, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do ano;
- O maior valor de faturamento ocorrido em um dia do ano;
- Número de dias no ano em que o valor de faturamento diário foi superior à média anual.

a) Considerar o vetor já carregado com as informações de valor de faturamento.

b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

c) Utilize o algoritmo mais veloz que puder definir.

**Reposta no main.py**

## 4) Banco de dados

Uma empresa solicitou a você um aplicativo para manutenção de um cadastro de clientes. Após a reunião de definição dos requisitos, as conclusões foram as seguintes:

- Um cliente pode ter um número ilimitado de telefones;
- Cada telefone de cliente tem um tipo, por exemplo: comercial, residencial, celular, etc. O sistema deve permitir cadastrar novos tipos de telefone;
- A princípio, é necessário saber apenas em qual estado brasileiro cada cliente se encontra. O sistema deve permitir cadastrar novos estados;

Você ficou responsável pela parte da estrutura de banco de dados que será usada pelo aplicativo. Assim sendo:

- Proponha um modelo lógico para o banco de dados que vai atender a aplicação. Desenhe as tabelas necessárias, os campos de cada uma e marque com setas os relacionamentos existentes entre as tabelas;
- Aponte os campos que são chave primária (PK) e chave estrangeira (FK);
- Faça uma busca utilizando comando SQL que traga o código, a razão social e o(s) telefone(s) de todos os clientes do estado de São Paulo (código “SP”);

**RESPOSTA**
**-- Tabela cliente
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razao_social VARCHAR(255) NOT NULL,
    estado CHAR(2) NOT NULL
);

-- Tabela telefone
CREATE TABLE telefone (
    id_telefone INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(20) NOT NULL,
    tipo_telefone VARCHAR(20) NOT NULL,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente)
);**

** relacionamento: cliente 1 <---- n telefone
Um cliente pode ter vários telefones

SELECT 
    c.id_cliente, 
    c.razao_social, 
    t.numero, 
    t.tipo_telefone 
FROM 
    cliente c
JOIN 
    telefone t ON c.id_cliente = t.cliente_id
WHERE 
    c.estado = 'SP'; **

## 5) Dois veículos, um carro e um caminhão, saem respectivamente de cidades opostas pela mesma rodovia. O carro, de Ribeirão Preto em direção a Barretos, a uma velocidade constante de 90 km/h, e o caminhão, de Barretos em direção a Ribeirão Preto, a uma velocidade constante de 80 km/h. Quando eles se cruzarem no percurso, qual estará mais próximo da cidade de Ribeirão Preto?

a) Considerar a distância de 125km entre a cidade de Ribeirão Preto <-> Barretos.
b) Considerar 3 pedágios como obstáculo e que o carro leva 5 minutos a mais para passar em cada um deles, pois ele não possui dispositivo de cobrança de pedágio.
c)Explique como chegou no resultado.

**RESPOSTA**
OBS: No enunciado pergunta apenas qual estará mais próximo e usando Km como parâmetros os dois terão a mesma distancia para Ribeirão preto.

Em relação ao tempo mais proximo de chegada para Ribeirão preto fiz os seguintes calculos.

Tempo do carro para percorrer todo o trajeto mais os 15 minutos de pedágio.
120km/ 90km = 1,333 = 80 minutos + 15 (pedagio) = 95 minutos

Camninhão tempo para percorrer.
120/ 80 = 1,5 = 90 minutos

Com esse valor o carro é mais lento que o caminhão.
Ao eles se encontrarem no percurso o tempo do carro por ser mais devagar, ele vai estar mais perto do seu local de origem que é Ribeirão Preto.
Então o carro é o mais próximo.

