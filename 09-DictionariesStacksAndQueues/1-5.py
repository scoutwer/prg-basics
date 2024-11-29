countries = [
{"name":"Poland", "population":38000000},
{"name": "USA", "population": 360000000},
{"name": "Brazil", "population": 209000000},
{"name": "Pakistan", "population": 212000000},
{"name": "Indonesia", "population": 220000000},
]

for i in countries:
    for key, value in i.items():
        print(f"{key}: {value}")