def log(msg):
  print(f"action log: {msg}")


with open("index.html", "w", encoding='utf-8') as file:
  texts = file.readlines()
  log(texts[0])
  texts[0] = str(int(texts[0].split(",")[0])+1) + ","
  log("changed.")
  log(texts[0])
  file.writelines(texts)

log("fin")
