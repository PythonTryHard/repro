Dependency: `hikari-lightbulb`

Note: Bot token shouldn't be relevant as bot errors out before `bot.run()`

Step to repro:
```
git clone https://github.com/PythonTryHard/repro
cd repro
python bot.py
```

and it should errors out when reloading saying "Sanity is already registered"
