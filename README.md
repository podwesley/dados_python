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

## 🚀 Como Usar

### 1. Configuração Básica

```python
# Configure os caminhos dos arquivos
INPUT_FILE = Path('seu_arquivo.csv')
OUTPUT_FILE = Path('saida.feature')

# Personalize o texto BDD (opcional)
BDD_TEXT = """Feature: Cenários de Teste Automatizados
  Como um usuário do sistema
  Eu quero executar cenários de teste
  Para validar as funcionalidades

  Scenario Outline: Validar dados
    Given que eu tenho os dados do cenário
    When eu executo o teste
    Then o resultado deve ser válido"""
```

### 2. Execução

```bash
python extrator.py
```

### 3. Saída Esperada

```
✅ Concluída! 150 linhas processadas. 📁 CSV: dados.csv → 📄 FEATURE: cenarios.feature
```

## 📁 Estrutura de Entrada

### Formato CSV Esperado

```csv
id,nome,idade,cidade,status
1,João Silva,25,São Paulo,ativo
2,Maria Santos,30,Rio de Janeiro,inativo
3,Pedro Oliveira,22,Belo Horizonte,ativo
4,Ana Costa,28,Salvador,ativo
```

### Requisitos
- ✅ Coluna `id` obrigatória (case-insensitive)
- ✅ Headers na primeira linha
- ✅ Suporte a delimitadores: `,`, `;`, `\t`
- ✅ Encoding UTF-8 com suporte a BOM

## 📄 Exemplos de Saída

### Formato BDD/Gherkin (.feature)

```gherkin
Feature: Cenários de Teste Automatizados
  Como um usuário do sistema
  Eu quero executar cenários de teste
  Para validar as funcionalidades

@1
Examples:
| nome        | idade | cidade      | status |
| João Silva  | 25    | São Paulo   | ativo  |

@2
Examples:
| nome         | idade | cidade         | status   |
| Maria Santos | 30    | Rio de Janeiro | inativo  |

@3
Examples:
| nome           | idade | cidade          | status |
| Pedro Oliveira | 22    | Belo Horizonte  | ativo  |
```

### Formato Markdown Simples

```markdown
| nome        | idade | cidade      | status |
| João Silva  | 25    | São Paulo   | ativo  |
| Maria Santos | 30    | Rio de Janeiro | inativo  |
| Pedro Oliveira | 22    | Belo Horizonte  | ativo  |
```

## ⚙️ Personalização Avançada

### 🎨 Modificar Formato de Saída

```python
# Formato BDD atual
output_f.write(f"@{linha[idx_id]}\nExamples:\n{header_formatado}\n{data_formatada}\n\n")

# Formato Markdown com ID
output_f.write(f"## Registro {linha[idx_id]}\n{data_formatada}\n\n")

# Formato TXT simples
output_f.write(f"ID: {linha[idx_id]} | {data_formatada}\n")

# Formato JSON-like
output_f.write(f'{{"id": "{linha[idx_id]}", "data": "{data_formatada}"}}\n')
```

### 🔍 Filtrar Colunas Específicas

```python
# Incluir apenas colunas específicas
colunas_desejadas = ['nome', 'idade', 'status']
outras_colunas = [(i, col) for i, col in enumerate(cabecalho) 
                 if i != idx_id and col in colunas_desejadas]

# Excluir colunas específicas
colunas_excluidas = ['campo_interno', 'temp']
outras_colunas = [(i, col) for i, col in enumerate(cabecalho) 
                 if i != idx_id and col not in colunas_excluidas]
```

### 🎛️ Controle de Headers

```python
# Repetir header a cada linha (atual)
for linha in leitor_csv:
    data_formatada = "| " + " | ".join(linha[i].ljust(larguras[i]) for i, _ in outras_colunas) + " |"
    output_f.write(f"@{linha[idx_id]}\nExamples:\n{header_formatado}\n{data_formatada}\n\n")

# Header único no início
output_f.write(f"{header_formatado}\n")
for linha in leitor_csv:
    data_formatada = "| " + " | ".join(linha[i].ljust(larguras[i]) for i, _ in outras_colunas) + " |"
    output_f.write(f"{data_formatada}\n")

# Sem headers
for linha in leitor_csv:
    data_formatada = "| " + " | ".join(linha[i].ljust(larguras[i]) for i, _ in outras_colunas) + " |"
    output_f.write(f"{data_formatada}\n")
```

## 🔧 Requisitos Técnicos

- **Python**: 3.6 ou superior
- **Bibliotecas**: 
  - `csv` (incluída)
  - `pathlib` (incluída)
- **Encoding**: UTF-8
- **Delimitadores suportados**: `,`, `;`, `\t`

## 📊 Performance e Otimizações

### ⚡ Características de Performance
- **Duas passadas**: Primeira para calcular larguras, segunda para escrever
- **Detecção automática**: Delimitador mais comum identificado automaticamente
- **Uso eficiente de memória**: Processa linha por linha
- **Encoding robusto**: Suporte completo a UTF-8 e BOM

### 📈 Benchmarks
- ✅ Validado com múltiplos modelos de IA
- ✅ Otimizado para arquivos grandes
- ✅ Uso de memória constante
- ✅ Processamento linear O(n)

## 🐛 Tratamento de Erros

### Tipos de Erro Tratados
```
❌ Erro: Arquivo CSV não encontrado em 'arquivo.csv'
❌ Erro inesperado: Coluna 'id' não encontrada no cabeçalho do CSV.
❌ Erro inesperado: 'utf-8' codec can't decode byte...
```

### Como Resolver
1. **Arquivo não encontrado**: Verifique o caminho e nome do arquivo
2. **Coluna ID ausente**: Adicione uma coluna 'id' ao seu CSV
3. **Problema de encoding**: Salve o arquivo como UTF-8

## 🎯 Casos de Uso Reais


### 📝 Documentação Técnica
```python
# Altere para formato Markdown
output_f.write(f"### Usuário {linha[idx_id]}\n{data_formatada}\n\n")
```

### 📋 Relatórios de Dados
```python
# Formato para relatórios
output_f.write(f"Registro #{linha[idx_id]}: {data_formatada}\n")
```

### 🔄 Migração de Dados
```python
# Formato SQL INSERT
colunas = [col for _, col in outras_colunas]
valores = [linha[i] for i, _ in outras_colunas]
output_f.write(f"INSERT INTO tabela ({', '.join(colunas)}) VALUES ('{\"', '\".join(valores)}');\n")
```

## 💡 Dicas e Truques

### 🔥 Dica 1: Linha Comentada Importante
```python
# output_f.write(f"{data_formatada}\n") # IMPORTANTE NÃO APAGAR!
```
Esta linha permite mudança rápida para formato simples quando necessário.

### 🔥 Dica 2: Debug de Delimitadores
```python
print(f"Delimitador detectado: '{delimitador}'")
```
Adicione esta linha para verificar qual delimitador foi detectado.

### 🔥 Dica 3: Visualizar Larguras
```python
print(f"Larguras calculadas: {larguras}")
```
Útil para entender o dimensionamento das colunas.

### 🔥 Dica 4: Backup Automático
```python
import shutil
if arquivo_saida.exists():
    shutil.copy(arquivo_saida, arquivo_saida.with_suffix('.bak'))
```

## 📚 Extensões Possíveis

### 🔮 Funcionalidades Futuras
- Suporte a Excel (.xlsx) nativo
- Interface gráfica (GUI)
- Configuração via arquivo JSON
- Templates de saída personalizáveis
- Validação de dados de entrada
- Logs detalhados
- Processamento em lote



## 📝 Notas do Desenvolvedor

Este extrator foi desenvolvido com auxílio de IA, mas **cada linha foi cuidadosamente revisada, debugada e testada manualmente**. A performance foi validada usando múltiplos modelos de IA (GPT-4, Sonnet-4, Gemini) para garantir uso otimizado de memória e recursos.

### 🎯 Filosofia de Desenvolvimento
- **Simplicidade**: Código limpo e fácil de entender
- **Flexibilidade**: Máxima customização com mínimo esforço  
- **Performance**: Eficiência sem comprometer funcionalidade
- **Robustez**: Tratamento completo de erros e edge cases

---

💻 **Desenvolvido com ❤️ e muita IA, mas debugado linha por linha com 🧠 humano!**