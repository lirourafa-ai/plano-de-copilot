# Data Assistant 🤖

Assistente simples de IA para análise de dados. Ideal para aprendizado e exploração rápida de datasets.

## Funcionalidades

- ✅ Carregar arquivos CSV e JSON
- ✅ Estatísticas descritivas (média, mediana, desvio padrão)
- ✅ Visualizar dados (primeiras linhas)
- ✅ Contar valores únicos por coluna
- ✅ Interface interativa por menu

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/lirourafa-ai/plano-de-copilot.git
cd plano-de-copilot
```

2. Python 3.7+ é necessário (sem dependências externas)

## Uso

Execute o assistente:
```bash
python data_assistant.py
```

### Exemplo Interativo
```
🤖 Assistente de Análise de Dados
========================================

Opções:
  1. Carregar arquivo (CSV/JSON)
  2. Info dos dados
  3. Estatísticas de coluna
  4. Ver primeiras linhas
  5. Contar valores únicos
  6. Sair

Escolha uma opção (1-6): 1
Caminho do arquivo: dados.csv
✅ Arquivo carregado: dados.csv
```

## Estrutura

```
plano-de-copilot/
├── data_assistant.py    # Código principal
└── README.md           # Este arquivo
```

## Próximas Iterações

- [ ] Suporte a mais formatos (Excel, Parquet)
- [ ] Gráficos (matplotlib/plotly)
- [ ] Filtros e queries
- [ ] Testes unitários
- [ ] API REST

## Autor

Rafael Liro - [GitHub](https://github.com/lirourafa-ai)

## Licença

MIT
