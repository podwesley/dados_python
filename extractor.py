import csv
from pathlib import Path

INPUT_FILE = Path('combinacoes_cenarios.csv')
OUTPUT_FILE = Path('cenarios.feature')
BDD_TEXT = """"""

def processar_csv_performatico(arquivo_csv: Path, arquivo_saida: Path):
    try:
        with arquivo_csv.open('r', encoding='utf-8', newline='') as arquivo:
            amostra = arquivo.read(2048)
            arquivo.seek(0)
            delimitador = max([',', ';', '\t'], key=amostra.count)

            leitor_csv = csv.reader(arquivo, delimiter=delimitador)

            cabecalho = [col.strip('\ufeff') for col in next(leitor_csv)]

            idx_id = next((i for i, col in enumerate(cabecalho) if col.lower() == 'id'), None)
            if idx_id is None:
                raise ValueError("Coluna 'id' não encontrada no cabeçalho do CSV.")

            outras_colunas = [(i, col) for i, col in enumerate(cabecalho) if i != idx_id]
            larguras = {i: len(col) for i, col in outras_colunas}

            for linha in leitor_csv:
                for idx, _ in outras_colunas:
                    if idx < len(linha):
                        larguras[idx] = max(larguras[idx], len(linha[idx]))

        with arquivo_csv.open('r', encoding='utf-8', newline='') as input_f, arquivo_saida.open('w', encoding='utf-8') as output_f:
            leitor_csv = csv.reader(input_f, delimiter=delimitador)
            next(leitor_csv)

            header_formatado = "| " + " | ".join(col.ljust(larguras[i]) for i, col in outras_colunas) + " |"
            output_f.write(f"{BDD_TEXT}\n")
            linhas_processadas = 0
            for linha in leitor_csv:
                data_formatada = "| " + " | ".join(linha[i].ljust(larguras[i]) for i, _ in outras_colunas) + " |"

                output_f.write(f"@{linha[idx_id]}\nExamples:\n{header_formatado}\n{data_formatada}\n\n")
                # output_f.write(f"{data_formatada}\n") # IMPORTANTE NÃO APAGAR!
                linhas_processadas += 1

        print(f"✅ Concluída! {linhas_processadas} linhas processadas. 📁 CSV: {arquivo_csv} → 📄 FEATURE: {arquivo_saida}")

    except FileNotFoundError:
        print(f"❌ Erro: Arquivo CSV não encontrado em '{arquivo_csv}'")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    processar_csv_performatico(INPUT_FILE, OUTPUT_FILE)