
# 📊 Análise de Vendas com Python

Este projeto demonstra uma análise simples de dados de vendas usando Python e bibliotecas como `pandas` e `matplotlib`.

## 📁 Dados utilizados

Os dados estão no arquivo `vendas.xlsx`, contendo colunas de data, produto e valor da venda.

## 🚀 O que o script faz

- Lê a planilha de dados (`vendas.xlsx`)
- Converte datas e extrai o mês de cada venda
- Agrupa e calcula o total de vendas por produto e por mês
- Gera dois gráficos:
  - Vendas por produto (barras)
  - Vendas por mês (linha)

## 🛠️ Tecnologias usadas

- Python 3
- pandas
- matplotlib

## 📌 Como executar

1. Baixe os arquivos `vendas.xlsx` e `analise_vendas.py`
2. Instale as bibliotecas necessárias (caso não tenha):

```bash
pip install pandas matplotlib openpyxl
```

3. Execute o script:

```bash
python analise_vendas.py
```

4. Serão gerados dois arquivos de imagem:
- `grafico_vendas_produto.png`
- `grafico_vendas_mes.png`

## 📈 Exemplos de saída (gráficos)

Esses gráficos representam os totais de vendas por produto e por mês.

---

Desenvolvido por **Marcos Iuri**
