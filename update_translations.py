
import json
import os

# Base English additions
additions_en = {
  "signals": {
    "empty": {
      "title": "Select a signal",
      "subtitle": "Click 'Brief' to see:",
      "list_1": "What triggered (plain English)",
      "list_2": "Two entry styles (pullback vs confirmation)",
      "list_3": "Risk guardrails (invalidation level)",
      "list_4": "Verified catalyst history",
      "reset": "Reset Filters"
    }
  },
  "movers": {
    "title": "Market Movers",
    "subtitle": "Live market movement—verified sources on every row. Scan with clarity.",
    "updating": "Updating...",
    "updated": "Updated",
    "categories": {
      "gainers": "Top Gainers",
      "losers": "Top Losers",
      "52wh": "52W High",
      "52wl": "52W Low",
      "prevday": "Prev Day",
      "all": "All Stocks"
    },
    "info": "Data is delayed by 15 minutes unless premium.",
    "howto": {
      "title": "How to use Market Movers",
      "gainers_desc": "Stocks with the biggest price increase/decrease today.",
      "52wh_desc": "Stocks hitting their highest/lowest price in the last year. Often signals breakout/breakdown.",
      "rsi_above": "RSI > 70: Potentially overbought (expensive).",
      "rsi_below": "RSI < 30: Potentially oversold (cheap).",
      "atr_desc": "Average True Range % shows how much the stock typically moves in a day. High ATR = higher risk/reward.",
      "got_it": "Got it"
    },
    "table": {
      "rsi": "RSI",
      "atr": "ATR%"
    }
  },
  "thesis": {
    "back_to_history": "Back to History",
    "day_horizon": "Day Horizon",
    "risk": "Risk",
    "confidence_score": "Confidence Score",
    "summary": {
      "title": "Summary",
      "why_now": "Why Buy Now?",
      "what_needs_happen": "What Needs to Happen",
      "main_worry": "Main Worry"
    },
    "trade_plan": {
      "title": "Trade Plan",
      "buying_strategy": "Buying Strategy",
      "scaling_in_desc": "\"Scaling In\" means buying in small chunks (e.g., 33% now, 33% later) instead of all at once. This reduces risk.",
      "rules_title": "Rules for Managing this Trade",
      "add_more": "Add More:",
      "take_profit": "Take Profit:",
      "time_limit": "Time Limit:",
      "safety_net_title": "Safety Net (Stop Loss)",
      "stop_loss_desc": "*If price hits this level, the trade idea is wrong. Sell immediately to protect your capital.",
      "how_much_invest": "How Much to Invest",
      "stop_loss": "Stop Loss (Exit)",
      "profit_goal": "Profit Goal",
      "buy_zone": "Buy Zone",
      "safety_net": "Safety Net",
      "reward": "Reward"
    }
  }
}

# Translations (simplified for key elements)
translations = {
    "fr": {
        "signals": {
            "empty": {
                "title": "Sélectionnez un signal",
                "subtitle": "Cliquez sur 'Brief' pour voir :",
                "list_1": "Ce qui a déclenché (en clair)",
                "list_2": "Deux styles d'entrée (repli vs confirmation)",
                "list_3": "Garde-fous (niveau d'invalidation)",
                "list_4": "Historique des catalyseurs vérifiés",
                "reset": "Réinitialiser les filtres"
            }
        },
        "movers": {
            "title": "Les Moteurs du Marché",
            "subtitle": "Mouvements de marché en direct — sources vérifiées. Scannez avec clarté.",
            "updating": "Mise à jour...",
            "updated": "Mis à jour",
            "categories": {
                "gainers": "Top Gagnants",
                "losers": "Top Perdants",
                "52wh": "Haut 52S",
                "52wl": "Bas 52S",
                "prevday": "Jour Préc",
                "all": "Toutes Actions"
            },
            "info": "Données différées de 15 min sauf premium.",
            "howto": {
                "title": "Comment utiliser",
                "gainers_desc": "Actions avec la plus forte hausse/baisse aujourd'hui.",
                "52wh_desc": "Plus haut/bas sur un an.",
                "rsi_above": "RSI > 70 : Potentiellement suracheté.",
                "rsi_below": "RSI < 30 : Potentiellement survendu.",
                "atr_desc": "ATR % montre la volatilité typique.",
                "got_it": "Compris"
            },
            "table": { "rsi": "RSI", "atr": "ATR%" }
        },
        "thesis": {
            "back_to_history": "Retour à l'historique",
            "day_horizon": "Horizon Jours",
            "risk": "Risque",
            "confidence_score": "Score de Confiance",
            "summary": {
                "title": "Résumé",
                "why_now": "Pourquoi acheter maintenant ?",
                "what_needs_happen": "Ce qui doit arriver",
                "main_worry": "Principale inquiétude"
            },
            "trade_plan": {
                "title": "Plan de Trade",
                "buying_strategy": "Stratégie d'Achat",
                "scaling_in_desc": "\"Scaling In\" signifie acheter par petits morceaux pour réduire le risque.",
                "rules_title": "Règles de gestion",
                "add_more": "Ajouter plus :",
                "take_profit": "Prendre profit :",
                "time_limit": "Limite de temps :",
                "safety_net_title": "Filet de Sécurité (Stop Loss)",
                "stop_loss_desc": "*Si le prix touche ce niveau, l'idée est fausse. Vendez immédiatement.",
                "how_much_invest": "Combien investir",
                "stop_loss": "Stop Loss",
                "profit_goal": "Objectif",
                "buy_zone": "Zone Achat",
                "safety_net": "Sécurité",
                "reward": "Récompense"
            }
        }
    },
    "es": {
        "signals": {
            "empty": {
                "title": "Seleccionar una señal",
                "subtitle": "Haga clic en 'Brief' para ver:",
                "list_1": "Qué lo activó (en lenguaje sencillo)",
                "list_2": "Dos estilos de entrada (retroceso vs confirmación)",
                "list_3": "Límites de riesgo (nivel de invalidación)",
                "list_4": "Historial de catalizadores verificados",
                "reset": "Restablecer filtros"
            }
        },
        "movers": {
            "title": "Motores del Mercado",
            "subtitle": "Movimiento del mercado en vivo. Escanea con claridad.",
            "updating": "Actualizando...",
            "updated": "Actualizado",
            "categories": {
                "gainers": "Top Ganadores",
                "losers": "Top Perdedores",
                "52wh": "Máx 52S",
                "52wl": "Mín 52S",
                "prevday": "Día Ant",
                "all": "Todas"
            },
            "info": "Datos retrasados 15 min excepto premium.",
            "howto": {
                "title": "Cómo usar",
                "gainers_desc": "Acciones con mayor subida/bajada hoy.",
                "52wh_desc": "Máximo/mínimo del último año.",
                "rsi_above": "RSI > 70: Potencialmente sobrecomprado.",
                "rsi_below": "RSI < 30: Potencialmente sobrevendido.",
                "atr_desc": "ATR % muestra la volatilidad típica.",
                "got_it": "Entendido"
            },
            "table": { "rsi": "RSI", "atr": "ATR%" }
        },
        "thesis": {
            "back_to_history": "Volver al historial",
            "day_horizon": "Horizonte (Días)",
            "risk": "Riesgo",
            "confidence_score": "Nivel de Confianza",
            "summary": {
                "title": "Resumen",
                "why_now": "¿Por qué comprar ahora?",
                "what_needs_happen": "Lo que debe suceder",
                "main_worry": "Preocupación principal"
            },
            "trade_plan": {
                "title": "Plan de Trading",
                "buying_strategy": "Estrategia de Compra",
                "scaling_in_desc": "\"Scaling In\" significa comprar en partes pequeñas para reducir el riesgo.",
                "rules_title": "Reglas de gestión",
                "add_more": "Añadir más:",
                "take_profit": "Tomar ganancias:",
                "time_limit": "Límite de tiempo:",
                "safety_net_title": "Red de Seguridad (Stop Loss)",
                "stop_loss_desc": "*Si el precio toca este nivel, vende inmediatamente.",
                "how_much_invest": "Cuánto invertir",
                "stop_loss": "Stop Loss",
                "profit_goal": "Objetivo",
                "buy_zone": "Zona Compra",
                "safety_net": "Seguridad",
                "reward": "Recompensa"
            }
        }
    },
     "de": {
        "signals": {
            "empty": {
                "title": "Signal auswählen",
                "subtitle": "Klicken Sie auf 'Brief' für Details:",
                "list_1": "Auslöser (einfach erklärt)",
                "list_2": "Zwei Einstiegsarten",
                "list_3": "Risikogrenzen",
                "list_4": "Verifizierte Katalysatoren",
                "reset": "Filter zurücksetzen"
            }
        },
        "movers": {
            "title": "Marktbewegungen",
            "subtitle": "Live-Marktdaten — verifizierte Quellen.",
            "updating": "Aktualisiere...",
            "updated": "Aktualisiert",
            "categories": {
                "gainers": "Top Gewinner",
                "losers": "Top Verlierer",
                "52wh": "52W Hoch",
                "52wl": "52W Tief",
                "prevday": "Vortag",
                "all": "Alle Aktien"
            },
            "info": "Daten 15 Min verzögert (außer Premium).",
            "howto": {
                "title": "Anleitung",
                "gainers_desc": "Aktien mit größter Änderung heute.",
                "52wh_desc": "Jahreshoch/-tief.",
                "rsi_above": "RSI > 70: Überkauft.",
                "rsi_below": "RSI < 30: Überverkauft.",
                "atr_desc": "ATR % zeigt typische Volatilität.",
                "got_it": "Verstanden"
            },
            "table": { "rsi": "RSI", "atr": "ATR%" }
        },
        "thesis": {
            "back_to_history": "Zurück zum Verlauf",
            "day_horizon": "Tage Horizont",
            "risk": "Risiko",
            "confidence_score": "Konfidenz",
            "summary": {
                "title": "Zusammenfassung",
                "why_now": "Warum jetzt kaufen?",
                "what_needs_happen": "Was passieren muss",
                "main_worry": "Hauptsorge"
            },
            "trade_plan": {
                "title": "Handelsplan",
                "buying_strategy": "Kaufstrategie",
                "scaling_in_desc": "Kaufen Sie in kleinen Tranchen, um das Risiko zu senken.",
                "rules_title": "Regeln für diesen Trade",
                "add_more": "Nachkaufen:",
                "take_profit": "Gewinnmitnahme:",
                "time_limit": "Zeitlimit:",
                "safety_net_title": "Sicherheitsnetz (Stop Loss)",
                "stop_loss_desc": "*Wenn der Preis dieses Niveau erreicht, sofort verkaufen.",
                "how_much_invest": "Investitionshöhe",
                "stop_loss": "Stop Loss",
                "profit_goal": "Ziel",
                "buy_zone": "Kaufzone",
                "safety_net": "Netz",
                "reward": "Chance"
            }
        }
    },
     "pt": {
        "signals": {
            "empty": {
                "title": "Selecione um sinal",
                "subtitle": "Clique em 'Brief' para ver:",
                "list_1": "O que acionou (em português claro)",
                "list_2": "Dois estilos de entrada",
                "list_3": "Limites de risco",
                "list_4": "Histórico verificado",
                "reset": "Redefinir Filtros"
            }
        },
        "movers": {
            "title": "Movimentadores",
            "subtitle": "Movimento do mercado ao vivo.",
            "updating": "Atualizando...",
            "updated": "Atualizado",
            "categories": {
                "gainers": "Maiores Altas",
                "losers": "Maiores Baixas",
                "52wh": "Máx 52S",
                "52wl": "Mín 52S",
                "prevday": "Dia Ant",
                "all": "Todas"
            },
            "info": "Dados com atraso de 15 min.",
            "howto": {
                "title": "Como usar",
                "gainers_desc": "Ações com maior variação hoje.",
                "52wh_desc": "Máxima/mínima de 52 semanas.",
                "rsi_above": "RSI > 70: Sobrecomprado.",
                "rsi_below": "RSI < 30: Sobrevendido.",
                "atr_desc": "ATR % mostra volatilidade típica.",
                "got_it": "Entendi"
            },
            "table": { "rsi": "RSI", "atr": "ATR%" }
        },
        "thesis": {
            "back_to_history": "Voltar ao Histórico",
            "day_horizon": "Horizonte (Dias)",
            "risk": "Risco",
            "confidence_score": "Pontuação de Confiança",
            "summary": {
                "title": "Resumo",
                "why_now": "Por que comprar agora?",
                "what_needs_happen": "O que precisa acontecer",
                "main_worry": "Principal preocupação"
            },
            "trade_plan": {
                "title": "Plano de Trade",
                "buying_strategy": "Estratégia de Compra",
                "scaling_in_desc": "Compre em partes pequenas para reduzir o risco.",
                "rules_title": "Regras de Gestão",
                "add_more": "Adicionar mais:",
                "take_profit": "Realizar lucro:",
                "time_limit": "Limite de tempo:",
                "safety_net_title": "Rede de Segurança (Stop Loss)",
                "stop_loss_desc": "*Se o preço atingir este nível, venda imediatamente.",
                "how_much_invest": "Quanto investir",
                "stop_loss": "Stop Loss",
                "profit_goal": "Alvo",
                "buy_zone": "Zona Compra",
                "safety_net": "Segurança",
                "reward": "Retorno"
            }
        }
    }
}

# Add partials for ja, ru, zh (using English fallback for complex sentences, translated headers)
translations["ja"] = {
    "signals": { "empty": { "title": "シグナルを選択", "subtitle": "詳細を見るには「Brief」をクリック:", "reset": "リセット" } },
    "movers": { "title": "市場の動き", "categories": { "gainers": "値上がり上位", "losers": "値下がり上位", "52wh": "52週高値", "52wl": "52週安値", "prevday": "前日", "all": "全銘柄" } },
    "thesis": { "back_to_history": "履歴に戻る", "summary": { "title": "概要", "why_now": "今買う理由は？" }, "trade_plan": { "title": "トレードプラン", "safety_net_title": "セーフティネット (損切り)" } }
}

translations["zh"] = {
    "signals": { "empty": { "title": "选择信号", "subtitle": "点击“简报”查看详情：", "reset": "重置筛选" } },
    "movers": { "title": "市场异动", "categories": { "gainers": "涨幅榜", "losers": "跌幅榜", "52wh": "52周新高", "52wl": "52周新低", "prevday": "前一日", "all": "所有股票" } },
    "thesis": { "back_to_history": "返回历史", "summary": { "title": "摘要", "why_now": "为何现在买入？" }, "trade_plan": { "title": "交易计划", "safety_net_title": "安全网 (止损)" } }
}

translations["ru"] = {
    "signals": { "empty": { "title": "Выберите сигнал", "subtitle": "Нажмите 'Brief' для просмотра:", "reset": "Сброс" } },
    "movers": { "title": "Лидеры рынка", "categories": { "gainers": "Лидеры роста", "losers": "Лидеры падения", "52wh": "52 нед. макс", "52wl": "52 нед. мин", "prevday": "Вчера", "all": "Все акции" } },
    "thesis": { "back_to_history": "Назад к истории", "summary": { "title": "Сводка", "why_now": "Почему покупать сейчас?" }, "trade_plan": { "title": "Торговый план", "safety_net_title": "Стоп-лосс" } }
}

def deep_merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value
    return destination

locales_dir = r"c:\Users\fishe\OneDrive\Documents\projectstock\public\locales"

for lang in ['en', 'fr', 'es', 'de', 'pt', 'ja', 'zh', 'ru']:
    file_path = os.path.join(locales_dir, lang, "translation.json")
    if not os.path.exists(file_path):
        print(f"Skipping {lang}, file not found")
        continue
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {lang}: {e}")
        data = {}

    # 1. Merge Base English (ensures structure exists)
    deep_merge(additions_en, data)

    # 2. Overwrite with specific translations if available
    if lang in translations:
        deep_merge(translations[lang], data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated {lang}")

