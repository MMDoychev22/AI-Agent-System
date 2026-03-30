from core import init_query_agent

agent = init_query_agent()

qs = [
    "Препоръчай ми научнофантастичен филм.",
    "Кои филми с Леонардо Ди Каприо имат висок рейтинг.",
    "Колко филма са след 2015 година.",
    "Искам нещо леко и забавно.",
    "Покажи ми филм на Кристофър Нолан.",
]

for q in qs:
    r = agent.ask(q)
    print("Q:", q)
    print("A:", r)
    print()
