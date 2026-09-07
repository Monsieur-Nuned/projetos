# ⚡ Calculadora de Consumo Energético de Eletrodomésticos

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg?logo=github)](https://github.com/)
[![Energy](https://img.shields.io/badge/Energia-Eficiência-orange.svg?logo=lightning&logoColor=white)](https://github.com/)

## 🎯 Nome e Objetivo do Sistema
* **Nome:** Calculadora de Consumo Energético de Eletrodomésticos
* **Objetivo:** Automatizar o cálculo do consumo mensal de energia elétrica (em kWh) e o custo financeiro estimado (em reais) de diferentes aparelhos eletrodomésticos, ajudando a compreender o impacto desses equipamentos na conta de luz.

---

## 💻 Linguagem Utilizada
* **Python**

---

## 📐 Fórmula Utilizada para o Cálculo

O sistema processa os dados inseridos através de duas fórmulas principais:

1. **Consumo Mensal (kWh):**
   $$\text{Consumo (kWh)} = \frac{\text{Potência (W)} \times \text{Tempo de Uso Diário (h)} \times 30 \text{ dias}}{1000}$$
   *(A divisão por 1.000 converte Watts para Quilowatts-hora, unidade padrão de cobrança das concessionárias).*

2. **Custo Mensal (R$):**
   $$\text{Custo (R\$)} = \text{Consumo Mensal (kWh)} \times \text{Tarifa de Energia (R\$ 0,68/kWh)}$$
