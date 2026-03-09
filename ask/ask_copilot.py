"""
ASK Copilot — Modo somente leitura.
Responde dúvidas, explica códigos, diagnostica erros e sugere abordagens.
Sem executar mudanças automaticamente.
"""

import re
from typing import Dict, List, Tuple


class AskCopilot:
    """Copiloto em modo ASK — diagnóstico e sugestões."""
    
    def __init__(self):
        self.knowledge_base = self._build_knowledge_base()
        self.history = []
    
    def _build_knowledge_base(self) -> Dict:
        """Base de conhecimento para diagnósticos comuns."""
        return {
            "undefined": {
                "resumo": "Isso quase sempre é uma variável vazia ou retorno de API.",
                "causa": [
                    "Array/objeto não inicializado",
                    "API retornou null ou vazio",
                    "Destructuring faltando validação"
                ],
                "como_confirmar": "Coloque um console.log() antes de acessar a propriedade.",
                "opcoes": [
                    "Adicione validação: if (foo && foo.prop)",
                    "Use optional chaining: foo?.prop",
                    "Inicialize no estado: const [data, setData] = useState([])"
                ]
            },
            "cors": {
                "resumo": "CORS bloqueou a requisição cross-origin.",
                "causa": [
                    "Header 'Access-Control-Allow-Origin' não definido",
                    "Método HTTP não permitido (POST/PUT/DELETE)",
                    "Credenciais enviadas sem Allow-Credentials"
                ],
                "como_confirmar": "Abra DevTools > Network, procure por 'cors' no status.",
                "opcoes": [
                    "Adicione middleware CORS no servidor",
                    "Use proxy em desenvolvimento",
                    "Configure headers corretos no backend"
                ]
            },
            "memory_leak": {
                "resumo": "Vazamento de memória — listeners não removidos ou refs acumulando.",
                "causa": [
                    "Event listeners não desinscritos",
                    "Timers não cancelados (setInterval)",
                    "Closures retendo dados grandes"
                ],
                "como_confirmar": "Use Chrome DevTools > Memory > Heap Snapshots.",
                "opcoes": [
                    "Limpe listeners em componentWillUnmount (React)",
                    "Cancele timers com clearInterval",
                    "Remova referências grandes após uso"
                ]
            },
            "typescript_type": {
                "resumo": "Erro de tipo — propriedade ou tipo não compatível.",
                "causa": [
                    "asserção de tipo muito específica",
                    "Interface/Type sem propriedade obrigatória",
                    "Union type necessita narrowing"
                ],
                "como_confirmar": "Leia a linha exata do erro TSC.",
                "opcoes": [
                    "Use 'as unknown as Type' com cuidado",
                    "Crie um Type Guard (função de verificação)",
                    "Estenda a Interface corretamente"
                ]
            }
        }
    
    def diagnose(self, error_message: str) -> Dict:
        """Diagnostica erro e retorna resposta estruturada."""
        error_lower = error_message.lower()
        
        # Busca por palavra-chave na base de conhecimento
        for key, content in self.knowledge_base.items():
            if key in error_lower:
                return self._format_response(key, content)
        
        # Se não encontrar, dá resposta genérica
        return {
            "resumo": "Não reconheço esse erro exatamente, mas vamos por passos.",
            "causa": ["Descrição incompleta ou erro não catalogado"],
            "como_confirmar": "Cole mais contexto: stack trace completo ou código relevante.",
            "opcoes": [
                "Tente debugar com console.log",
                "Rode em um ambiente controlado",
                "Consulte a documentação oficial da lib"
            ],
            "precisa_de_ajuda": True
        }
    
    def _format_response(self, key: str, content: Dict) -> Dict:
        """Formata resposta estruturada."""
        return {
            "categoria": key,
            "resumo": content["resumo"],
            "causa_provavel": content["causa"],
            "como_confirmar": content["como_confirmar"],
            "opcoes": content["opcoes"]
        }
    
    def explain_code(self, code_snippet: str, language: str = "python") -> Dict:
        """Explica o que um trecho de código faz."""
        lines = code_snippet.strip().split('\n')
        explanations = []
        
        for i, line in enumerate(lines, 1):
            line_stripped = line.strip()
            
            if not line_stripped or line_stripped.startswith('#'):
                continue
            
            explanation = self._explain_line(line_stripped, language)
            explanations.append({
                "linha": i,
                "código": line_stripped,
                "explicação": explanation
            })
        
        return {
            "resumo": f"Analisando {len(explanations)} linha(s) de {language}.",
            "linhas": explanations,
            "padrão_detectado": self._detect_pattern(code_snippet, language)
        }
    
    def _explain_line(self, line: str, language: str) -> str:
        """Explica uma linha de código."""
        if language == "python":
            if "def " in line:
                return "Define uma função."
            elif "import " in line:
                return "Importa um módulo/biblioteca."
            elif "=" in line and "==" not in line:
                return "Atribuição de valor a uma variável."
            elif "for " in line:
                return "Inicia um loop iterativo."
            elif "if " in line:
                return "Condicional — executa se verdadeiro."
        
        elif language == "javascript":
            if "function " in line or "=>" in line:
                return "Define uma função."
            elif "const " in line or "let " in line:
                return "Declara uma variável."
            elif "async" in line:
                return "Marca esta função como assíncrona."
            elif "await " in line:
                return "Aguarda a resolução de uma Promise."
        
        return "Qualidade de código não analisável automaticamente."
    
    def _detect_pattern(self, code: str, language: str) -> List[str]:
        """Detecta padrões de design."""
        patterns = []
        
        if "try" in code and "except" in code or "catch" in code:
            patterns.append("Tratamento de erros (try/catch)")
        
        if "class " in code:
            patterns.append("Programação orientada a objetos (OOP)")
        
        if "async" in code and "await" in code:
            patterns.append("Programação assíncrona")
        
        if "if" in code and "else" in code:
            patterns.append("Controle condicional")
        
        return patterns if patterns else ["Código linear/simples"]
    
    def suggest_approach(self, problem: str) -> Dict:
        """Sugere abordagens para um problema."""
        suggestions = {
            "autenticação": [
                "JWT armazenado em httpOnly cookie",
                "OAuth2 com terceiros (Google, GitHub)",
                "Sessão com servidor (Redis)"
            ],
            "performance": [
                "Profile com DevTools/profiler",
                "Lazy loading e code splitting",
                "Cache com CDN ou service workers"
            ],
            "testes": [
                "Testes unitários (Jest, Vitest)",
                "Testes de integração (Supertest)",
                "E2E com Cypress/Playwright"
            ],
            "deploy": [
                "Docker + Kubernetes",
                "Serverless (AWS Lambda, Vercel)",
                "CI/CD com GitHub Actions"
            ]
        }
        
        problem_lower = problem.lower()
        matched = None
        
        for key in suggestions:
            if key in problem_lower:
                matched = key
                break
        
        if matched:
            return {
                "problema": problem,
                "categoria": matched,
                "abordagens": suggestions[matched],
                "proxima_pergunta": f"Qual dessas abordagens combina com seu contexto?"
            }
        
        return {
            "problema": problem,
            "aviso": "Não reconheço exatamente esse problema.",
            "sugestao": "Cole mais detalhes (stack, ambiente, versões)."
        }
    
    def ask(self, user_input: str) -> Dict:
        """Interface principal — responde a qualquer pergunta."""
        self.history.append({"usuario": user_input})
        
        # Detecta tipo de pergunta
        if "error" in user_input.lower() or "erro" in user_input.lower():
            return self.diagnose(user_input)
        
        elif "explain" in user_input.lower() or "explica" in user_input.lower():
            # Extrai código se houver
            return {"resposta": "Cole o código no próximo input e eu explico linha por linha."}
        
        elif "approach" in user_input.lower() or "como fazer" in user_input.lower():
            return self.suggest_approach(user_input)
        
        else:
            return {
                "resposta": "Ok. Você pode me perguntar sobre: erros, explicar código, ou sugerir abordagens.",
                "exemplos": [
                    "Tenho um erro 'undefined is not an object'",
                    "Explica esse trecho de código",
                    "Como fazer autenticação em Node?"
                ]
            }


def main():
    """Menu interativo do ASK Copilot."""
    copilot = AskCopilot()
    
    print("🤖 ASK Copilot — Modo Somente Leitura")
    print("=" * 50)
    print("Diagnóstico, explicações e sugestões (sem editar).\n")
    
    while True:
        print("\nVocê pode:")
        print("  • Descrever um erro")
        print("  • Pedir para explicar código")
        print("  • Pedir sugestões (abordagem)")
        print("  • 'sair' para terminar\n")
        
        user_input = input("Você: ").strip()
        
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("\n👋 Até logo!")
            break
        
        if not user_input:
            print("⚠️  Digite algo para continuar.")
            continue
        
        response = copilot.ask(user_input)
        
        # Formata resposta
        print("\n📋 Cortana (ASK):")
        for key, val in response.items():
            if isinstance(val, list):
                print(f"  {key}:")
                for item in val:
                    print(f"    • {item}")
            else:
                print(f"  {key}: {val}")


if __name__ == "__main__":
    main()
