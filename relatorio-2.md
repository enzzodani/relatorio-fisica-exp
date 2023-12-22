# *Objetivos*
---
* [x] Poucas palavras, explicar o experimento

# *Hipóteses, aproximações e modelos de medição*
* [x] Modelo de medição (conservação eq)
---
$$
m_1x_1=m_1x_1'+m_2x_2'
$$
---
* [x] Explicar os termos da equação

# *Análise dos resultados das medições*

* [x] $x_1 \rightarrow$ flutuação, média dos lançamentos (tipo A),desvio padrão da média 
  x/ = 14.76 incerteza = 0.18
* [x] $x_1' \rightarrow$ flutuação, média dos lançamentos (tipo A),desvio padrão da média
  x/=8.566667 incerteza = 0.13
* [x] $x_2' \rightarrow$ flutuação, média dos lançamentos (tipo A),desvio padrão da média
  x/ = 5.153333 incerteza = 0.27 
* [x] $m_1 \rightarrow$ tipo B, resolução / raiz de 3
m/ = 04.00 incerteza = 0.58
* [x] $m_2 \rightarrow$ tipo B, resolução / raiz de 3
  m/ = 10.00 incerteza = 0.58

## *equações*

$$
u_y = \sqrt{\sum^{n}_{i=1} [\frac{\partial F}{\partial x_i}]²\sigma_i²}
$$
---
$$
A (m_1,x_1) = m_1*x_1 = 04,00*14,76 = 59,0 \text{ } g*cm
$$
---
$$
u_A = \sqrt{[\frac{\partial A}{\partial m_1}]²\sigma_{m_1}² + [\frac{\partial A}{\partial x_1}]²\sigma_{x_1}²} = \sqrt{[x_1]²\sigma_{m_1}² + [m_1]²\sigma_{x_1}²}
$$
---
$$
u_A = \sqrt{[14,76]²*0,58² + [4,00]²*0,18²} = 8,6\text{ } g*cm
$$
---
$$
A = ( \pm ) g*cm
$$
---
$$
B (m_1,x_1',m_2,x_2') = m_1*x_1' + m_2*x_2' = 04,00*08,57 + 10,00*05,15 = 85,7 \text{ } g*cm
$$
---
$$
B (m_1,x_1', m_2,x_2') = m_1*x_1' + m_2*x_2' \rightarrow \text{tipo C, derivadas parciais} 
$$
----
$$
u_B = \sqrt{[\frac{\partial B}{\partial m_1}]²\sigma_{m_1}² + [\frac{\partial B}{\partial x_1'}]²\sigma_{x_1'}²+ [\frac{\partial B}{\partial m_2}]²\sigma_{m_2}² + [\frac{\partial B}{\partial x_2'}]²\sigma_{x_2'}²} = \sqrt{[x_1']²\sigma_{m_1}² + [m_1]²\sigma_{x_1'}²+ [x_2']²\sigma_{m_2}² + [m_2]²\sigma_{x_2'}²}
$$
---
$$
u_B = \sqrt{[08,57]²*0,58² + [04,00]²*0,13²+ [05,15]²*0,58² + [10,00]²0,27²} = 6,4 \text{ } g*cm
$$

## *teste de compatibilidade*

* [ ] $\frac{|A - B|}{\sqrt{u_A²+u_B²}} \leq 2,5$

---
$$
\frac{|A - B|}{\sqrt{u_A²+u_B²}} = \frac{|59,0 - 85,7|}{\sqrt{8,6²+6,4²}} = 2,49\leq 2,5 \rightarrow \text{A e B são compatíveis.}
$$
---
* [ ] Falar se A e B são compatíveis ou discrepantes

# *Conclusão*
* [x] Falar se o experimento de fato provou a conservação do momento linear ou não


