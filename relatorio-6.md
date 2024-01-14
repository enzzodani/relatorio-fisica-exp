# Dados do CSV

h1  ; 21.6 ; 0.1
h21 ; 100 ; 0.5
h22 ; 120 ; 0.5
h23 ; 140 ; 0.5
DX-h21 ; DX-h22 ; DX-h23
68.90  ; 75.60  ; 80.10
69.50  ; 76.30  ; 80.80
69.60  ; 77.00  ; 80.90
69.70  ; 77.00  ; 81.00
70.00  ; 76.50  ; 81.00
70.10  ; 77.50  ; 81.20
70.00  ; 77.90  ; 81.20
70.60  ; 76.70  ; 81.40
70.70  ; 76.90  ; 81.60
70.20  ; 77.00  ; 81.60
70.20  ; 76.80  ; 81.50
69.90  ; 77.00  ; 81.90
69.90  ; 77.20  ; 81.90
70.30  ; 77.30  ; 82.20
70.70  ; 77.50  ; 82.50
70.30  ; 77.40  ; 82.70
70.70  ; 77.60  ; 82.30
70.40  ; 77.60  ; 82.20
70.70  ; 77.70  ; 82.00
71.00  ; 77.60  ; 82.00
70.50  ; 77.90  ; 82.90
70.60  ; 77.90  ; 82.10
70.40  ; 77.00  ; 82.10
70.30  ; 77.40  ; 82.00
70.60  ; 77.70  ; 82.20
70.70  ; 77.30  ; 81.60
70.30  ; 77.40  ; 81.80
70.40  ; 77.00  ; 82.00
70.30  ; 77.50  ; 82.10
69.90  ; 77.40  ; 81.70

frequencia dx-h21 = 1.05
frequencia dx-h22 = 1.15
frequencia dx-h23 = 1.40

# Objetivos do Experimento

Neste experimento, exploraremos a Conservação de Energia Mecânica por meio da comparação entre dois modelos de medição propostos e os resultados obtidos experimentalmente. A análise desses dados será conduzida com o emprego de médias ponderadas, visando a uma compreensão mais precisa e crítica das relações energéticas envolvidas. Essa abordagem aprofundará a análise da concordância entre teoria e experimento, desenvolvendo habilidades analíticas e interpretativas fundamentais em nosso estudo de física.

# Hipóteses, aproximações e modelo de medição

## Hipóteses

## Aproximações

## Modelo de Medição

$$
\Delta x = \sqrt{\gamma h_1 h_2}
$$

# Análise dos resultados das medições

* [x] h1 = $(21,600 \pm 0,058) cm$ 
* [x] Escreva explicitamente a expressão da incerta de gama dependente das variaǘeis h1, h2i, e delta X

$$
\Delta x = \sqrt{\gamma h_1 h_2} \rightarrow \gamma = \frac{\Delta x²}{h_1h_2}
$$

$$
\frac{\partial (\frac{\Delta x²}{h_1h_2})}{\partial h1}$$

$$
u_y = \sqrt{\sum^{n}_{i=1} [\frac{\partial F}{\partial x_i}]²\sigma_i²} \rightarrow u_{\gamma} = \sqrt{(\frac{\partial \gamma}{\partial h_1})²\sigma_{h_1}² + (\frac{\partial \gamma}{\partial h_2})²\sigma_{h_2}² + (\frac{\partial \gamma}{\partial \Delta x})²\sigma_{\Delta x}²} 

\newline

= \sqrt{(-\frac{ \Delta x²}{h_1²h_2})²\sigma_{h_1}² + (-\frac{\Delta x²}{h_1h_2²})²\sigma_{h_2}² + (\frac{2\Delta x}{h_1h_2})²\sigma_{\Delta x}²} = \frac{\Delta x}{h_1h_2}\sqrt{\frac{\Delta x²}{h_1²}\sigma_{h_1}² + \frac{\Delta x²}{h_2²}\sigma_{h_2}² + 4\sigma_{\Delta x}²}
$$

## Situação 1
* [x] $h_{21}$ (Inceteza tipo B) = $(100 \pm 0.29)$ cm
* [x] $\Delta x_1$ (Incerteza tipo A) = $(70,247 \pm 0.081)$ cm 
* [x] $\gamma_1$ (Incerteza tipo C) = $(2,285 \pm 0,010)$ 

$$
\gamma_1 = \frac{\Delta x_1²}{h_1h_{21}} = \frac{70,247²}{(21,600)(100)} = 2,285
$$

$$
u_{\gamma_1} = \frac{\Delta x_1}{h_1h_{21}}\sqrt{(\frac{\Delta x_1}{h_1})²\sigma_{h_1}² + (\frac{\Delta x_1}{h_{21}})²\sigma_{h_{21}}² + 4\sigma_{\Delta x_1}²} =

\newline \rightarrow \newline

= \frac{70,247}{(21,600)  (100)}\sqrt{(\frac{70,247}{21,600})² 0,058² + (\frac{70,247}{100})²0,29² + 4(0,081)²} = 0,010
$$

## Situação 2
* [x] $h_{22}$ (Inceteza tipo B) = $(120 \pm 0.29)$ cm
* [x] $\Delta x_2$ (Incerteza tipo A) = $(77,220 \pm 0,093)$ cm 
* [x] $\gamma_2$ (Incerteza tipo C) = $(2,300 \pm 0,010)$ 

$$
u_{\gamma_2} = \frac{\Delta x_2}{h_1h_{22}}\sqrt{(\frac{\Delta x_2}{h_1})²\sigma_{h_1}² + (\frac{\Delta x_2}{h_{22}})²\sigma_{h_{22}}² + 4\sigma_{\Delta x_2}²} = \frac{77,220^2}{(21,600)(120)}\sqrt{(\frac{77,220}{21,600})²\sigma_{0,058}² + (\frac{77,220}{120})²\sigma_{0,29}² + 4\sigma_{0,093}²} = 0,010
$$

## Situação 3
* [x] $h_{23}$ (Inceteza tipo B) = $(140 \pm 0.29)$ cm
* [x] $\Delta x_3$ (Incerteza tipo A) = $(81,75 \pm 0,11)$ cm 
* [x] $\gamma_3$ (Incerteza tipo C) = $(2,2100 \pm 0,0096)$ 

$$
u_{\gamma_3} = \frac{\Delta x_3}{h_1h_{23}}\sqrt{(\frac{\Delta x_3}{h_1})²\sigma_{h_1}² + (\frac{\Delta x_3}{h_{23}})²\sigma_{h_{23}}² + 4\sigma_{\Delta x_3}²} = \frac{81,75^2}{(21,600)(140)}\sqrt{(\frac{81,75}{21,600})²\sigma_{0,058}² + (\frac{81,75}{140})²\sigma_{0,29}² + 4\sigma_{0,11}²} = 0,0096
$$

* [ ] Obtenha o valor mais provável de gamma e sua incerteza através do cálculo da média ponderada com base nos valores obtidos nas situações 1, 2 e 3

### Pesos
$$
p_{1}=\frac{1}{0,010^2}=10000
p_{2}=\frac{1}{0,010^2}=10000
p_{3}=\frac{1}{0,0096^2}=10850,6944
$$

### Incerteza da Média Ponderada

$$
u_{\gamma_{mp}}=\frac{1}{\sqrt{p_{1}+p_{2}+p_{3}}}=\frac{1}{\sqrt{10000+10000+10850,6944}}=0,0057
$$

### Média Ponderada

$$
\gamma_{mp}=\frac{\gamma{1}\times p_{1}+\gamma{2}\times p_{2}+\gamma{3}\times p_{3}}{p_{1}+p_{2}+p_{3}}=\frac{2,285\times 10000+2,300\times 10000+2,2100\times 10850,6944}{10000+10000+10850,6944}=2,2635
$$

* [x] gamma medido $\gamma_m = (2,2635 \pm 0,0057)$   

# Teste de compatibilidade
* [x] Confira se γ é compatível ou discrepante com 4 e 20/7 (OBS: Como γ = 4 ou 20/7 são números exatos sua incerteza é nula)

$$
\frac{|2,2635 - 4|}{\sqrt{(0,0057)^2}} = 304,64912 \leq 2,5 \text{ são discrepantes}
$$
$$
\frac{|2,2635 - \frac{20}{7}|}{\sqrt{(0,0057)^2}} = 104,14787 \leq 2,5 \text{ são discrepantes}
$$

# Conclusões
