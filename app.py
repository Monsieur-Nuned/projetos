Eletrodoméstico = input("diga seu aparelho: ")
potencia = float(input("diga a potencia em watts: "))
uso = float(input("tempo medio de uso em horas por dia: "))
consumo_m = (potencia * uso * 30) / 1000 
custo = float(consumo_m * 0.68)
print ("seu(a)", Eletrodoméstico, "consome,", consumo_m,
        "de energia por mês, tendo um valor de em média", 
       custo, "reais mensais")
