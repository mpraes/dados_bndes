import pandas as pd
import io

df = pd.read_csv("https://dadosabertos.bndes.gov.br/dataset/3bd6b9f4-f803-4e5c-889b-4cefdf9f1543/resource/30f458c0-75d2-4ab1-8218-9a9fa748c1fd/download/compras-contratos-administrativos-contratos-administrativos.csv", sep=';', decimal=',', encoding='UTF-8')

nome_arquivo = 'compras-contratos-administrativos-contratos-administrativos.csv'

print("Estas são as colunas:", df.columns.to_list())

# Calcula quantidade total de linhas e colunas do dataframe
num_rows, num_cols = df.shape
print("Quantidade de linhas:", num_rows)
print("Quantidade de colunas:", num_cols)

# Verifica a quantidade de valores não nulos por coluna
non_null_counts = df.count()
non_null_counts_df = pd.DataFrame({'Quantidade de valores não nulos por coluna': non_null_counts})

# Verifica se há valores nulos em cada coluna
null_counts = df.isnull().sum()
null_counts_df = pd.DataFrame({'Quantidade de valores nulos por coluna': null_counts})

# Cria um pequeno DataFrame combinando os resultados das duas consultas
results_df = pd.concat([non_null_counts_df, null_counts_df], axis=1)

# Exibe o pequeno DataFrame no console
print(results_df)

# Verifica os valores únicos (distintos) por coluna
unique_values = df.nunique()
unique_values_df = pd.DataFrame({'Quantidade de valores únicos por coluna': unique_values})

# Mostra algumas estatísticas descritivas sobre as colunas numéricas
print("\nEstatísticas descritivas das colunas numéricas:")
print(df.describe())

# Mostra informações gerais sobre o DataFrame
print("\nInformações gerais sobre o DataFrame:")
print(df.info())

# Verifica os valores mais frequentes em cada coluna
most_frequent_values = df.mode().iloc[0]
most_frequent_values_df = pd.DataFrame({'Valores mais frequentes por coluna': most_frequent_values})

# Abre o arquivo txt em modo de escrita
with open('perfil_dados.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write("Perfil dos Dados do arquivo: " + nome_arquivo + "\n")
    arquivo.write("------------------------------------------------------------------\n")

    # Calcula quantidade total de linhas e colunas do dataframe
    num_rows, num_cols = df.shape
    arquivo.write("Quantidade de linhas: {}\n".format(num_rows))
    arquivo.write("Quantidade de colunas: {}\n".format(num_cols))
    arquivo.write("------------------------------------------------------------------\n")

    # Verifica a quantidade de valores não nulos por coluna
    non_null_counts = df.count()
    arquivo.write("Quantidade de valores não nulos por coluna:\n")
    arquivo.write(non_null_counts.to_string())
    arquivo.write("\n------------------------------------------------------------------\n")

    # Verifica se há valores nulos em cada coluna
    null_counts = df.isnull().sum()
    arquivo.write("Quantidade de valores nulos por coluna:\n")
    arquivo.write(null_counts.to_string())
    arquivo.write("\n------------------------------------------------------------------\n")

    # Verifica os valores únicos (distintos) por coluna
    unique_values = df.nunique()
    arquivo.write("Quantidade de valores únicos por coluna:\n")
    arquivo.write(unique_values.to_string())
    arquivo.write("\n------------------------------------------------------------------\n")

    # Mostra algumas estatísticas descritivas sobre as colunas numéricas
    arquivo.write("Estatísticas descritivas das colunas numéricas:\n")
    arquivo.write(df.describe().to_string())
    arquivo.write("\n------------------------------------------------------------------\n")

  # Mostra informações gerais sobre o DataFrame
    arquivo.write("Informações gerais sobre o DataFrame:\n")
    buffer = io.StringIO()
    df.info(buf=buffer)
    arquivo.write(buffer.getvalue())
    arquivo.write("\n------------------------------------------------------------------\n")

    # Verifica os valores mais frequentes em cada coluna
    most_frequent_values = df.mode().iloc[0]
    arquivo.write("Valores mais frequentes por coluna:\n")
    arquivo.write(most_frequent_values.to_string())
    arquivo.write("\n------------------------------------------------------------------\n")

print("Perfil dos dados exportado para 'perfil_dados.txt'.")