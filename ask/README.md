# ASK Copilot 📋

Copiloto técnico em **modo somente leitura**. Diagnóstico, explicações e sugestões — sem editar arquivos automaticamente.

## O que faz

- **Diagnostica erros** — Analisa messages de erro e sugere causas prováveis
- **Explica código** — Linha por linha, padrões detectados
- **Sugere abordagens** — Para problemas de autenticação, performance, testes, deploy
- **Menu interativo** — Pergunte naturalmente

## Como usar

```bash
python ask/ask_copilot.py
```

### Exemplos de entrada

1. **Diagnosticar erro:**
   ```
   Tenho um erro "TypeError: Cannot read property 'map' of undefined"
   ```
   Ele retorna: resumo, causa provável, como confirmar, 2–3 opções.

2. **Explicar código:**
   ```
   Explica esse trecho:
   def load_csv(path):
       with open(path) as f:
           data = list(csv.DictReader(f))
       return data
   ```
   Retorna: análise linha por linha + padrão detectado.

3. **Sugerir abordagem:**
   ```
   Como fazer autenticação em Node.js?
   ```
   Retorna: 3 abordagens (JWT, OAuth2, sessão) + próximo passo.

## Estrutura

```
ask/
├── ask_copilot.py      # Lógica principal
└── README.md           # Este arquivo
```

## Personalidade — Cortana

- Tom calmo, direto, um toque de humor
- Máximo 2 perguntas se faltar contexto
- Sempre declara suposições
- Indica riscos/impactos quando relevante

## Base de conhecimento

Atualmente cobre:
- `undefined` — variáveis vazias
- `cors` — requisições cross-origin
- `memory_leak` — vazamento de memória
- `typescript_type` — erros de tipo

Expandível.

## Próximas iterações

- [ ] Integração com Stack Overflow
- [ ] Diagnóstico via stack trace completo
- [ ] Logs de sessão
- [ ] Persistência de histórico
- [ ] Suportar mais linguagens (TypeScript, Go, Rust)

---

**Modo:** ASK (somente leitura). Sem executar mudanças.
