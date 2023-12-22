# *Objetivos*
---
* [x] Poucas palavras, explicar o experimento

# *Hipóteses, aproximações e modelos de medição*
* [x] Modelo de medição 
---
$$
\mu_e(L_1,L_2) = \tan(\theta) = \frac{L_2}{L_1}
$$
---
* [ ] Explicar os termos da equação

# *Análise dos resultados das medições*

* [x] $L_1 \rightarrow 30.05 in 0.29\text{ incerteza tipo B, resolução do instrumento sobre raiz de 3, é o mesmo para as 3 situações}$
* [x] $L_2^{A} \rightarrow 11.73 in 0,33\text{}$
* [x] $L_2^{B} \rightarrow 14.53 in 0.21\text{}$
* [x] $L_2^{C} \rightarrow 15.22in0.22\text{}$


## *equações*
* [x] Equações A
---
$$
u_{\mu_e}^{A}=\frac{L_2^{A}}{L_1^{A}}\sqrt{(\frac{\sigma_{L_1^{A}}}{L_1^{A}})²+(\frac{\sigma_{L_2^{A}}}{L_2^{A}})²} = \frac{11,73}{30,05}\sqrt{(\frac{0,29}{30,05})²+(\frac{0,33}{11,73})²} = 0,012
$$
---
$$
\mu_e^{A}(L_1^{A},L_2^{A}) = \tan(\theta) = \frac{L_2^{C}}{L_1^{C}} = \frac{11,73}{30,05} = 0,390
$$
---
* [x] Equações B
---
$$
u_{\mu_e}^{B}=\frac{L_2^{B}}{L_1^{B}}\sqrt{(\frac{\sigma_{L_1^{B}}}{L_1^{B}})²+(\frac{\sigma_{L_2^{B}}}{L_2^{B}})²} = \frac{14,53}{30,05}\sqrt{(\frac{0,29}{30,05})²+(\frac{0,21}{14,53})²} = 0,0084
$$
---
$$
\mu_e^{B}(L_1^{B},L_2^{B}) = \tan(\theta) = \frac{L_2^{B}}{L_1^{B}} = \frac{14,53}{30,05} = 0,4835
$$
---
* [x] Equações C
---
$$
u_{\mu_e}^{C}=\frac{L_2^{C}}{L_1^{C}}\sqrt{(\frac{\sigma_{L_1^{C}}}{L_1^{C}})²+(\frac{\sigma_{L_2^{C}}}{L_2^{C}})²} = \frac{15,22}{30,05}\sqrt{(\frac{0,29}{30,05})²+(\frac{0,22}{15,22})²} = 0,0088
$$
---
---
$$
\sigma_{\mu_{e}} = \sqrt{(\frac{\partial \mu_e}{\partial L_1})²\sigma²_{L_1} + (\frac{\partial \mu_e}{\partial L_2})²\sigma²_{L_2}}
$$
---
$$
\sigma_{\mu_{e}} = \sqrt{(\frac{-L_2}{L²_1})²\sigma²_{L_1} + (\frac{1}{ L_1})²\sigma²_{L_2}} = \sqrt{\frac{L_2²}{L⁴_1}\sigma²_{L_1} + \frac{1}{ L_1²}\sigma²_{L_2}} = \frac{L_2}{L_1}\sqrt{(\frac{\sigma_{L_1}}{L_1})²+(\frac{\sigma_{L_2}}{L_2})²}
$$
---
$$
u_{\mu_e}^{C}=\frac{L_2^{C}}{L_1^{C}}\sqrt{(\frac{\sigma_{L_1^{C}}}{L_1^{C}})²+(\frac{\sigma_{L_2^{C}}}{L_2^{C}})²} = \frac{15,22}{30,05}\sqrt{(\frac{0,29}{30,05})²+(\frac{0,22}{15,22})²} = 0,0088
$$
---

---
$$
\frac{11,72}{30,05}\sqrt{\left(\frac{0,28}{30,\:05}\right)²+\left(\frac{0,\:33}{11,\:72}\right)²}
$$
---
$$
\mu_e^{C}(L_1^{C},L_2^{C}) = \tan(\theta) = \frac{L_2^{C}}{L_1^{C}} = \frac{15,2}{30,05} = 0,5065
$$
---

## *teste de compatibilidade*
---
$$
\frac{|\mu_e^{A} - \mu_e^{C}|}{\sqrt{(u_{\mu_e}^{A})^2+(u_{\mu_e}^{C})^2}} \leq 2,5 \rightarrow \frac{|0,390 - 0,5065|}{\sqrt{(0,012)^2+(0,0088)^2}} = 7,823 \text{ ,logo A e C são discrepantes}
$$
---
$$
\frac{|\mu_e^{A} - \mu_e^{B}|}{\sqrt{(u_{\mu_e}^{A})^2+(u_{\mu_e}^{B})^2}} \leq 2,5 \rightarrow \frac{|0,390 - 0,4835|}{\sqrt{(0,012)^2+(0,0084)^2}} = 6,38318 \text{ , logo A e B são discrepantes}
$$
---
$$
\frac{|\mu_e^{B} - \mu_e^{C}|}{\sqrt{(u_{\mu_e}^{B})^2+(u_{\mu_e}^{C})^2}} \leq 2,5 \rightarrow \frac{|0,4835 - 0,5065|}{\sqrt{(0,0084)^2+(0,0088)^2}} = 1,89 \text{ ,logo B e C são compatíveis}
$$
---
* [x] Falar se A e B são compatíveis ou discrepantes
* [x] Falar se A e C são compatíveis ou discrepantes
* [x] Falar se B e C são compatíveis ou discrepantes

# *Conclusão*
* [ ] 


