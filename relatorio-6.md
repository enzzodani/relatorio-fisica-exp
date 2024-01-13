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

* [x] h1 = $(21,6 \pm 0,058) cm$ 
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
* [x] $\Delta x_1$ (Incerteza tipo A) = $(70,24667 \pm 0.081)$ cm 
* [ ] $\gamma_1$ (Incerteza tipo C) = $( \pm )$ 

## Situação 2
* [x] $h_{22}$ (Inceteza tipo B) = $(120 \pm 0.29)$ cm
* [ ] $\Delta x_2$ (Incerteza tipo A) = $( \pm )$ cm 
* [ ] $\gamma_2$ (Incerteza tipo C) = $( \pm )$ 

## Situação 3
* [x] $h_{23}$ (Inceteza tipo B) = $(140 \pm 0.29)$ cm
* [ ] $\Delta x_3$ (Incerteza tipo A) = $( \pm )$ cm 
* [ ] $\gamma_3$ (Incerteza tipo C) = $( \pm )$ 

* [ ] Obtenha o valor mais provável de gamma e sua incerteza através do cálculo da média ponderada com base nos valores obtidos nas situações 1, 2 e 3

* [ ] $\gamma = ( \pm )$   

# Teste de compatibilidade
* [ ] Confira se γ é compatível ou discrepante com 4 e 20/7 (OBS: Como γ = 4 ou 20/7 são números exatos sua incerteza é nula)

$$
\frac{|_{} - _{}|}{\sqrt{(u_{})^2+(u_{})^2}} = \leq 2,5
$$

# Conclusões
