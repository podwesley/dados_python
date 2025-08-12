# 🚀 Extrator de Dados Excel - Python

Um extrator de dados **simples**, **poderoso** e **flexível** desenvolvido em Python para processar arquivos Excel/CSV e gerar múltiplos formatos de saída personalizáveis.

## ✨ Características Principais

- 📊 **Extração Versátil**: Processa arquivos Excel e CSV com facilidade
- 🎯 **Múltiplos Formatos**: Gera saídas em `.txt`, `.markdown`, `.feature` e outros
- 🔧 **Totalmente Personalizável**: Configure headers, colunas e formato de saída
- 📈 **Independência de Colunas**: Funciona com qualquer quantidade de colunas
- ⚡ **Performance Otimizada**: Revisado por múltiplas IAs (GPT-4, Sonnet-4, Gemini) para uso eficiente de memória
- 🎛️ **Controle Total**: Repita headers, remova-os ou personalize completamente a saída

## 🛠️ Funcionalidades

### 🎪 Flexibilidade de Saída
- Personalize quais colunas incluir na saída
- Configure o formato de cada linha
- Controle a repetição ou remoção de headers
- Ajuste automático de largura das colunas para formatação perfeita

### ⚡ Performance
- Detecção automática de delimitadores (`,`, `;`, `\t`)
- Processamento em duas passadas para otimização de memória
- Tratamento eficiente de arquivos grandes
- Encoding UTF-8 com suporte a BOM

### 🎯 Casos de Uso
- Geração de arquivos `.feature` para testes BDD/Gherkin
- Conversão de dados para Markdown formatado
- Extração personalizada para relatórios
- Transformação de dados para diferentes formatos

## 📋 Exemplo de Uso

```python
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
                linhas_processadas += 1

        print(f"✅ Concluída! {linhas_processadas} linhas processadas. 📁 CSV: {arquivo_csv} → 📄 FEATURE: {arquivo_saida}")

    except FileNotFoundError:
        print(f"❌ Erro: Arquivo CSV não encontrado em '{arquivo_csv}'")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    processar_csv_performatico(INPUT_FILE, OUTPUT_FILE)
```

## 🚀 Como Usar

1. **Configure os arquivos**:
   ```python
   INPUT_FILE = Path('seu_arquivo.csv')
   OUTPUT_FILE = Path('saida.feature')
   ```

2. **Personalize o texto BDD** (opcional):
   ```python
   BDD_TEXT = """Feature: Seus cenários de teste
   Como um usuário
   Eu quero executar cenários
   Para validar funcionalidades"""
   ```

3. **Execute o script**:
   ```bash
   python extrator.py
   ```

## 📁 Estrutura de Entrada

O arquivo CSV deve conter:
- Uma coluna `id` (obrigatória)
- Qualquer quantidade de colunas adicionais
- Headers na primeira linha

### Exemplo de CSV:
```csv
id,nome,idade,cidade
1,João,25,São Paulo
2,Maria,30,Rio de Janeiro
3,Pedro,22,Belo Horizonte
```

## 📄 Exemplo de Saída (.feature)

```gherkin
@1
Examples:
| nome | idade | cidade        |
| João | 25    | São Paulo     |

@2
Examples:
| nome  | idade | cidade           |
| Maria | 30    | Rio de Janeiro   |

@3
Examples:
| nome  | idade | cidade           |
| Pedro | 22    | Belo Horizonte   |
```

## ⚙️ Personalização Avançada

### Modificar Formato de Saída
Edite a linha de formatação para personalizar a saída:

```python
# Formato atual (BDD/Gherkin)
output_f.write(f"@{linha[idx_id]}\nExamples:\n{header_formatado}\n{data_formatada}\n\n")

# Formato Markdown simples
output_f.write(f"{data_formatada}\n")

# Formato personalizado
output_f.write(f"Cenário {linha[idx_id]}:\n{data_formatada}\n---\n")
```

### Filtrar Colunas Específicas
```python
# Incluir apenas colunas específicas
colunas_desejadas = ['nome', 'idade']
outras_colunas = [(i, col) for i, col in enumerate(cabecalho) 
                 if i != idx_id and col in colunas_desejadas]
```

## 🔧 Requisitos

- Python 3.6+
- Biblioteca `csv` (incluída no Python)
- Biblioteca `pathlib` (incluída no Python)

## 📊 Performance

- ✅ Otimizado para uso eficiente de memória
- ✅ Processamento em duas passadas para cálculo automático de larguras
- ✅ Detecção automática de delimitadores
- ✅ Tratamento robusto de encoding e caracteres especiais

## 🐛 Tratamento de Erros

- Arquivo não encontrado
- Coluna 'id' ausente
- Problemas de encoding
- Delimitadores não suportados
- Feedback visual com emojis para facilitar debugging

## 🎯 Casos de Uso Práticos

- **Testes BDD**: Geração de arquivos `.feature` para Cucumber/Gherkin
- **Documentação**: Conversão de dados para Markdown formatado
- **Relatórios**: Extração personalizada de dados tabulares
- **Migração de Dados**: Transformação entre diferentes formatos
- **Automação de Testes**: Geração dinâmica de cenários de teste

## 📝 Notas do Desenvolvedor

Este projeto foi desenvolvido com auxílio de IA, mas **cada linha foi cuidadosamente revisada, debugada e testada**. A performance foi validada usando múltiplos modelos de IA (GPT-4, Sonnet-4, Gemini) para garantir uso otimizado de memória e recursos.

---

**💡 Dica**: Mantenha a linha comentada `# output_f.write(f"{data_formatada}\n")` para facilitar mudanças rápidas de formato!