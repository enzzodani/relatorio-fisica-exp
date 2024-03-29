# Dados do CSV

m     ; 040 ; Massa suspensa em g
Ma    ; 702 ; Massa do anel em g
Mp    ; 704 ; Massa da placa em g
Res_B ; 001 ; Resolução da balança em g
H     ; 074 ; Altura da massa suspensa em cm
dH    ; 0.5 ; Resolução da medida da altura da massa suspensa em cm
d (cm); 004 ; Diâmetro do disco da base no qual se enrola o fio em cm.
Res_d ; 0.005 ; Resolução da medida do diâmetro do disco da base em cm
d_int ; 10.8 ; Diâmetro interno do anel em (cm)
d_ext ; 12.7 ; Diâmetro externo do anel (cm)
dr    ; 0.1 ; Resolução da medida dos diâmetros do anel em cm
Lp    ; 5.05 ; Largura da placa em cm. Deve ser medida com a régua
Lc    ; 22.6 ; Comprimento da placa em cm. Deve ser medida com a régua
dR    ; 0.1 ; Resolução da régua em cm.
dt    ; 0.01 ; Resolução do cronômetro em s
t_base; t_anel (s) ; t_placa (s)
11.89 ; 13.10 ; 13.06
11.87 ; 13.43 ; 13.08
12.25 ; 12.93 ; 12.54
12.36 ; 13.10 ; 13.01
12.37 ; 13.69 ; 13.00
11.80 ; 13.69 ; 12.63
12.20 ; 12.96 ; 12.98
12.35 ; 13.26 ; 12.95
11.49 ; 13.13 ; 12.75
12.54 ; 13.28 ; 13.46
12.54 ; 13.46 ; 12.78
12.30 ; 13.44 ; 13.50
11.64 ; 13.72 ; 12.79
11.75 ; 12.62 ; 12.82
11.76 ; 12.97 ; 12.71
12.04 ; 12.66 ; 13.18
12.28 ; 12.63 ; 13.33
12.25 ; 12.35 ; 13.31
11.84 ; 13.24 ; 13.00
11.29 ; 13.60 ; 13.00
12.01 ; 12.80 ; 13.00
11.94 ; 12.94 ; 12.52
12.96 ; 13.36 ; 12.47
12.44 ; 13.34 ; 12.54
11.80 ; 13.43 ; 12.86
11.91 ; 13.72 ; 13.20
11.47 ; 13.26 ; 13.08
11.37 ; 13.78 ; 13.45
12.14 ; 13.60 ; 13.03
12.09 ; 13.56 ; 13.03
               

# Objetivos do Experimento

O presente experimento tem como objetivo explorar e comparar os resultados obtidos para o momento de inércia de um objeto. Para isso, será realizado um confronto entre os dados obtidos por meio de um modelo de medição específico, apresentado na seção subsequente, e outro modelo derivado da solução da integral que define o momento de inércia. A análise comparativa busca verificar a equivalência entre esses métodos de medição, proporcionando uma abordagem abrangente para compreender o comportamento rotacional dos sólidos em estudo.

# Hipóteses, aproximações e modelo de medição

Uma hipótese central para este experimento é a expectativa de que o momento de inércia do modelo dinâmico será equivalente ao momento de inércia do modelo estático.Além disso, é importante considerar as aproximações adotadas nos modelos de medição, reconhecendo eventuais simplificações necessárias para facilitar a análise. A precisão e confiabilidade dos resultados dependerão da fidelidade dessas aproximações em relação ao comportamento real dos sólidos em rotação, sendo crucial avaliar a influência dessas simplificações nos resultados finais. Os modelos de medições utilizados serão:

Modelo de medição Dinâmico
$$
I_d = \frac{md²g}{8h}(t²-t²_{base})
$$

Modelo de medição estático
$$
I_{anel} = \frac{M(D²_1+D_2²)}{8}
$$
$$
I_{placa} = \frac{M(L²_1+L_2²)}{12}
$$

# Análise dos resultados das medições

## Incertezas medidas
### Modelo Dinâmico

* $h = (0,7400 \pm 0,0029)$ m
* $d = (0,040000 \pm 0,000029)$ m
* $m = (0,04000 \pm 0,00058)$ Kg
* $t_o = (12,030 \pm 0,070)$ s
* $t_p = (12,969 \pm 0,051)$ s
* $t_a = (13,226 \pm 0,071)$ s

### Modelo Estático Placa
* $M = ( \pm )$ Kg
* $L_1 = ( \pm )$ m
* $L_2 = ( \pm )$ m

### Modelo Estático Anel
* $M = ( \pm )$ Kg
* $D_1 = ( \pm )$ m
* $D_2 = ( \pm )$ m


## Análise de incertezas


* A analise da incerteza do modelo dinâmico deve levar em conta apenas 3 variáveis no modelo dinâmico: massa, tempo e tempo base

$$
u_{Id} = \sqrt{[\frac{\partial I_d}{\partial m}]²\sigma_m² + [\frac{\partial I_d}{\partial t}]²\sigma_t² + [\frac{\partial I_d}{\partial t_0}]²\sigma_{t_0}²} 
$$

$$
=\sqrt{[\frac{d²g}{8h}(t²-t²_0)]²\sigma_m² + [\frac{md²g}{8h}(2t)]²\sigma_t² + [\frac{md²g}{8h}(-2t_{0})]²\sigma_{t_{0}}²}
$$

$$
= \frac{I_d}{(t²-t²_{0})}\sqrt{[\frac{(t²-t_{0}²)}{m}\sigma_m]²+4(t²\sigma_t²+t²_{0}\sigma_{0}²)}
$$

* Análise da incerteza do modelo estático do anel

$$
u_{I_{anel}} = \sqrt{[\frac{\partial I_a}{\partial D_1}]²\sigma_{D_1}² + [\frac{\partial I_a}{\partial D_2}]²\sigma_{D_2}² + [\frac{\partial I_a}{\partial M}]²\sigma_{M}²}
$$

$$
= \sqrt{[\frac{D_1M}{4}]²\sigma_{D_1}² + [\frac{D_2M}{4}]²\sigma_{D_2}² + [\frac{D_1²+D_2²}{8}]²\sigma_{M}²}
$$

$$
= \frac{2I_a}{D_1²+D_2²}\sqrt{(D_1\sigma_{D_1})²+(D_2\sigma_{D_2})²+(\frac{D_1²+D_2²}{2M}\sigma_M)²}
$$

* Análise da incerteza do modelo estático do anel

$$
u_{I_{placa}} = \sqrt{[\frac{\partial I_p}{\partial L_1}]²\sigma_{L_1}² + [\frac{\partial I_p}{\partial L_2}]²\sigma_{L_2}² + [\frac{\partial I_p}{\partial M}]²\sigma_{M}²}
$$

$$
= \sqrt{[\frac{L_1M}{6}]²\sigma_{L_1}² + [\frac{L_2M}{6}]²\sigma_{L_2}² + [\frac{L_1²+L_2²}{12}]²\sigma_{M}²}
$$

$$
= \frac{2I_p}{L_1²+L_2²}\sqrt{(L_1\sigma_{L_1})²+(L_2\sigma_{L_2})²+(\frac{L_1²+L_2²}{2M}\sigma_M)²}
$$

# Teste de compatibilidade

## I da Placa Dinâmico x I da Placa Estático

$$
\frac{|I_{d} - I_{e}|}{\sqrt{(u_{I_d})^2+(u_{I_e})^2}} = \frac{| - |}{\sqrt{()^2+()^2}}\leq 2,5
$$

## I do Anel Dinâmico x I do Anel Estático

$$
\frac{|I_{d} - I_{e}|}{\sqrt{(u_{I_d})^2+(u_{I_e})^2}} = \frac{| - |}{\sqrt{()^2+()^2}}\leq 2,5
$$

# Conclusões
