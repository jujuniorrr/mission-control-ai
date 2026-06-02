# ============================================
# MISSION CONTROL AI
# Global Solution - FIAP
# ============================================

# Nome da missão
nome_missao = "Orion Test Alpha"

# Nome da equipe
nome_equipe = "Graph Orbit"

# Áreas monitoradas
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Matriz principal da missão
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa"

    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"

    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"

    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"
resultado = analisar_temperatura(39)
print(resultado)

def analisar_comunicacao(valor):

    if valor < 30:
        return "CRÍTICO", 2, "Comunicação em nível crítico"

    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"

    else:
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(valor):

    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"

    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"

    else:
        return "NORMAL", 0, "Energia estável"

def analisar_oxigenio(valor):

    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"

    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"

    else:
        return "NORMAL", 0, "Oxigênio adequado"

def analisar_estabilidade(valor):

    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"

    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"

    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"

def classificar_ciclo(pontos):

    if pontos <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontos <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(pontos):

    if pontos <= 2:
        return "Manter operação normal e continuar monitoramento."

    elif pontos <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    else:
        return "Ativar modo de segurança e priorizar sistemas críticos."
riscos_ciclos = []
riscos_por_area = [0, 0, 0, 0, 0]

for i, ciclo in enumerate(dados_missao):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    temp_status = analisar_temperatura(temperatura)
    com_status = analisar_comunicacao(comunicacao)
    bat_status = analisar_bateria(bateria)
    oxi_status = analisar_oxigenio(oxigenio)
    est_status = analisar_estabilidade(estabilidade)

    print(f"Ciclo {i+1}")
    print(temp_status)
    print(com_status)
    print(bat_status)
    print(oxi_status)
    print(est_status)
    pontuacao_total = (
            temp_status[1] +
            com_status[1] +
            bat_status[1] +
            oxi_status[1] +
            est_status[1]
    )

    print(f"Pontuação: {pontuacao_total}")

    riscos_ciclos.append(pontuacao_total)

    riscos_por_area[0] += temp_status[1]
    riscos_por_area[1] += com_status[1]
    riscos_por_area[2] += bat_status[1]
    riscos_por_area[3] += oxi_status[1]
    riscos_por_area[4] += est_status[1]

    classificacao = classificar_ciclo(pontuacao_total)
    recomendacao = gerar_recomendacao(pontuacao_total)

    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")

ciclo_mais_critico = riscos_ciclos.index(max(riscos_ciclos)) + 1

maior_risco = max(riscos_ciclos)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

if riscos_ciclos[-1] > riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de piora."

elif riscos_ciclos[-1] < riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de melhora."

else:
    tendencia = "A missão permaneceu estável."
indice_area = riscos_por_area.index(max(riscos_por_area))

area_mais_afetada = areas_monitoradas[indice_area]

print("\n" + "=" * 50)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 50)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")

print(f"Risco médio: {risco_medio:.2f}")

print(f"Tendência: {tendencia}")

print(f"Área mais afetada: {area_mais_afetada}")
