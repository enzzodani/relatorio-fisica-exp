# *Objetivos*
---
* [x] Poucas palavras, explicar o experimento

# *Hipóteses, aproximações e modelos de medição*
* [ ] Hipóteses: O que se espera achar => gravidade do IBGE
* [ ] Aproximações
* [ ] Modelo de medição 
---
$$
g(l,T) = 4\pi²\frac{l}{T²}
$$
---
* [ ] Explicar os termos da equação

# *Análise dos resultados das medições*
* [x] L1: tipo B m incerteza:0,029 valor: 1,150
* [x] T1: tipo A s incerteza: 0,0039 valor: 2,1264 (in 3,919149377 x10 -03 v=2,1263667)
* [x] L2: tipo B m incerteza: 0,029 valor: 1,450
* [x] T2: tipo A s incerteza: 0,0046 valor: 2,3992
* [x] L3: tipo B m incerteza: 0,029 valor: 1,750
* [x] T3: tipo A s incerteza: 0,0051 valor: 2,6391


## *equações*
---
$$
u_y = \sqrt{\sum^{n}_{i=1} [\frac{\partial F}{\partial x_i}]²\sigma_i²}
$$
---
Fórmula geral das incertezas da gravidade
$$
u_{g} = \sqrt{[\frac{\partial g}{\partial l}]²\sigma_{l}² + [\frac{\partial g}{\partial T}]²\sigma_{T}²} \rightarrow u_{g} = \sqrt{[\frac{4\pi²}{T²}]²\sigma_{l}² + [\frac{- 8\pi² \times l}{T³}]²\sigma_{T}²}
$$
$$
\rightarrow u_g = \frac{4\pi²}{T²}\sqrt{\sigma²_l + \frac{4l²}{T²}\sigma²_T}
$$
---
### Caso 1
---
$$
g(l_1,T_1) = 4\pi²\frac{l_1}{T_1²} = 4\pi²\frac{1,150}{2,1264²} = 10,04\frac{m}{s²}
$$
---
$$
u_{g_1} = \frac{4\pi²}{T_1²}\sqrt{\sigma²_{l_1} + \frac{4l_1²}{T_1²}\sigma²_{T_1}} = \frac{4\pi²}{2,1264²}\sqrt{(0,029)² + \frac{4(1,150)²}{(2,1264)²}(0,0039)²} = 0,26\frac{m}{s²}
$$
---
### Caso 2
---
$$
g(l_2,T_2) = 4\pi²\frac{l_2}{T_2²} = 4\pi²\frac{1,450}{2,3992²} = 9,94\frac{m}{s²}
$$
---
$$
u_{g_2} = \frac{4\pi²}{T_2²}\sqrt{\sigma²_{l_2} + \frac{4l_2²}{T_2²}\sigma²_{T_2}} = \frac{4\pi²}{2,3992²}\sqrt{(0,029)² + \frac{4(1,450)²}{(2,3992)²}(0,0046)²} = 0,20\frac{m}{s²}
$$
---
### Caso 3
---
$$
g(l_3,T_3) = 4\pi²\frac{l_3}{T_3²} = 4\pi²\frac{1,750}{2,6391²} = 9,92\frac{m}{s²}
$$
---
$$
u_{g_3} = \frac{4\pi²}{T_3²}\sqrt{\sigma²_{l_3} + \frac{4l_3²}{T_3²}\sigma²_{T_3}} = \frac{4\pi²}{2,6391²}\sqrt{(0,029)² + \frac{4(1,750)²}{(2,6391)²}(0,0051)²} = 0,17 \frac{m}{s²}
$$
---
## *teste de compatibilidade*
* [x] Verificar se g1 e g2 são compatíveis ou discrepantes
* [X] Verificar se g1 e g3 são compatíveis ou discrepantes
* [x] Verificar se g2 e g3 são compatíveis ou discrepantes
* [x] A partir dos valores de g obtidos, determine um único valor para a acelaração da gravidade local com sua incerteza, por meio de uma média ponderada
* [x] Verificar se gmp é compativel ou discrepante com g = (9.782028 +- 0.000023)m/s²
$$
\frac{|g_1 - g_2|}{\sqrt{(u_{g_1})^2+(u_{g_2})^2}} = \frac{|10,04 - 9,94|}{\sqrt{(0,26)^2+(0,20)^2}} = 0,3 \leq 2,5  \rightarrow g_1 \text{ e } g_2 \text{ são compatíveis}
$$
---
$$
\frac{|g_1 - g_3|}{\sqrt{(u_{g_1})^2+(u_{g_3})^2}} = \frac{|10,04 - 9,92|}{\sqrt{(0,26)^2+(0,17)^2}} = 0,39\leq 2,5 \rightarrow g_1\text{ e }g_3 \text{ são compatíveis}
$$
---
$$
\frac{|g_3 - g_2|}{\sqrt{(u_{g_3})^2+(u_{g_2})^2}} = \frac{|9,92 - 9,94|}{\sqrt{(0,17)^2+(0,20)²}} = 0,07\leq 2,5 \rightarrow g_2 \text{ e }g_3 \text{ são compatíveis}
$$
---
### média ponderada

peso1
$$
p_1=\frac{1}{u_{g_1}²} = \frac{1}{0,26²} = 14,8 
$$
---
peso2
$$
p_2=\frac{1}{u_{g_2}²} = \frac{1}{0,20²} = 25,0
$$
---
peso3
$$
p_3=\frac{1}{u_{g_3}²} = \frac{1}{0,17²} = 34,6
$$
---
media ponderada, valor pincipal
$$
g_{mp}=\frac{g_1\times p_1+g_2\times p_2+g_3\times p_3}{p_1+p_2+p_3} = \frac{10,04\times 14,8 +9,94\times 25,0+9,92\times 34,6}{14,8+25,0+34,6} = 9,95 \text{ }m/s²
$$
$$
u_{g_{mp}} = \frac{1}{\sqrt{p_1+p_2+p_3}}= \frac{1}{\sqrt{14,8+25,0+34,6}} = 0,12 \text{ } m/s²
$$
---
$$
\frac{|g_{mp} - g_{ibge}|}{\sqrt{(u_{g_{mp}})^2+(u_{g_{ibge}})^2}} = \frac{|9,950000 - 9,782028|}{\sqrt{(0,120000)^2+(0,000023)^2}} = 1,39 \leq 2,5 \rightarrow g_{mp} \text{ e } g_{ibge} \text{ são compatíveis}
$$
---


# *Conclusão*
* [x] Fazer a conclusão


