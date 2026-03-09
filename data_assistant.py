"""
Assistente de IA simples para análise de dados.
Modo estudo: carrega dados e responde perguntas básicas.
"""

import json
import csv
import statistics
from pathlib import Path


class DataAssistant:
    """Assistente simples de análise de dados."""
    
    def __init__(self):
        self.data = None
        self.filename = None
    
    def load(self, filepath):
        """Carrega arquivo CSV ou JSON."""
        path = Path(filepath)
        
        if not path.exists():
            print(f"❌ Arquivo não encontrado: {filepath}")
            return False
        
        try:
            if path.suffix.lower() == '.csv':
                self._load_csv(path)
            elif path.suffix.lower() == '.json':
                self._load_json(path)
            else:
                print("❌ Formato não suportado. Use CSV ou JSON.")
                return False
            
            self.filename = path.name
            print(f"✅ Arquivo carregado: {self.filename}")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao carregar: {e}")
            return False
    
    def _load_csv(self, path):
        """Carrega CSV e converte para lista de dicts."""
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.data = list(reader)
    
    def _load_json(self, path):
        """Carrega JSON."""
        with open(path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def info(self):
        """Mostra info básica dos dados."""
        if self.data is None:
            print("⚠️  Nenhum dado carregado.")
            return
        
        print(f"\n📊 Info do arquivo '{self.filename}':")
        print(f"   Linhas: {len(self.data)}")
        
        if isinstance(self.data, list) and self.data:
            if isinstance(self.data[0], dict):
                cols = list(self.data[0].keys())
                print(f"   Colunas: {', '.join(cols)}")
    
    def stats(self, column):
        """Calcula estatísticas para uma coluna numérica."""
        if self.data is None:
            print("⚠️  Nenhum dado carregado.")
            return
        
        try:
            # Extrai valores numéricos da coluna
            values = []
            for row in self.data:
                if isinstance(row, dict):
                    val = row.get(column)
                else:
                    val = row
                
                if val is not None:
                    try:
                        values.append(float(val))
                    except (ValueError, TypeError):
                        pass
            
            if not values:
                print(f"❌ Coluna '{column}' não tem valores numéricos.")
                return
            
            print(f"\n📈 Estatísticas para '{column}':")
            print(f"   Contagem: {len(values)}")
            print(f"   Média: {statistics.mean(values):.2f}")
            print(f"   Mediana: {statistics.median(values):.2f}")
            print(f"   Desvio padrão: {statistics.stdev(values):.2f}" if len(values) > 1 else "")
            print(f"   Mínimo: {min(values):.2f}")
            print(f"   Máximo: {max(values):.2f}")
        
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    def head(self, n=5):
        """Mostra as primeiras n linhas."""
        if self.data is None:
            print("⚠️  Nenhum dado carregado.")
            return
        
        print(f"\n📋 Primeiras {n} linhas:")
        for i, row in enumerate(self.data[:n]):
            print(f"   {i+1}: {row}")
    
    def count_values(self, column):
        """Conta valores únicos de uma coluna."""
        if self.data is None:
            print("⚠️  Nenhum dado carregado.")
            return
        
        try:
            values = {}
            for row in self.data:
                if isinstance(row, dict):
                    val = row.get(column)
                else:
                    val = row
                
                if val is not None:
                    values[val] = values.get(val, 0) + 1
            
            print(f"\n🔢 Contagem de valores em '{column}':")
            for val, count in sorted(values.items(), key=lambda x: x[1], reverse=True):
                print(f"   {val}: {count}")
        
        except Exception as e:
            print(f"❌ Erro: {e}")


def main():
    """Menu interativo."""
    assistant = DataAssistant()
    
    print("🤖 Assistente de Análise de Dados")
    print("=" * 40)
    
    while True:
        print("\nOpções:")
        print("  1. Carregar arquivo (CSV/JSON)")
        print("  2. Info dos dados")
        print("  3. Estatísticas de coluna")
        print("  4. Ver primeiras linhas")
        print("  5. Contar valores únicos")
        print("  6. Sair")
        
        choice = input("\nEscolha uma opção (1-6): ").strip()
        
        if choice == "1":
            filepath = input("Caminho do arquivo: ").strip()
            assistant.load(filepath)
        
        elif choice == "2":
            assistant.info()
        
        elif choice == "3":
            column = input("Nome da coluna: ").strip()
            assistant.stats(column)
        
        elif choice == "4":
            try:
                n = int(input("Quantas linhas? (padrão 5): ") or "5")
                assistant.head(n)
            except ValueError:
                print("❌ Insira um número válido.")
        
        elif choice == "5":
            column = input("Nome da coluna: ").strip()
            assistant.count_values(column)
        
        elif choice == "6":
            print("\n👋 Até logo!")
            break
        
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
