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
* A analise da incerteza deve levar em conta apenas 3 variáveis no modelo dinâmico: massa, tempo e tempo base

$$
u_y = \sqrt{\sum^{n}_{i=1} [\frac{\partial F}{\partial x_i}]²\sigma_i²} \rightarrow u_{Id} = \sqrt{[\frac{\partial I_d}{\partial m}]²\sigma_m² + [\frac{\partial I_d}{\partial t}]²\sigma_t² + [\frac{\partial F}{\partial t_{base}}]²\sigma_{t_{base}}²}
$$

# Teste de compatibilidade
$$
\frac{|_{} - _{}|}{\sqrt{(u_{})^2+(u_{})^2}} =
$$

# Conclusões
