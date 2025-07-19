
import pandas as pd
import matplotlib.pyplot as plt

# Lê a planilha de vendas
df = pd.read_excel("vendas.xlsx")

# Converte a coluna "Data" para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Adiciona coluna "Mês"
df["Mês"] = df["Data"].dt.strftime("%Y-%m")

# Total de vendas por produto
vendas_por_produto = df.groupby("Produto")["Valor"].sum()

# Total de vendas por mês
vendas_por_mes = df.groupby("Mês")["Valor"].sum()

# Gráfico de vendas por produto
plt.figure(figsize=(8, 5))
vendas_por_produto.plot(kind="bar", color="skyblue")
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Valor Total (R$)")
plt.tight_layout()
plt.savefig("grafico_vendas_produto.png")
plt.close()

# Gráfico de vendas por mês
plt.figure(figsize=(8, 5))
vendas_por_mes.plot(marker="o", color="orange")
plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Valor Total (R$)")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_vendas_mes.png")
plt.close()

print("Gráficos gerados com sucesso!")
