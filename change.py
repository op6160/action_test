def log(msg):
  print(f"action log: {msg}")
#test

with open("index.html", "r", encoding='utf-8') as file:
  texts = file.readlines()
  log(texts[0])
  texts[0] = str(int(texts[0].split(",")[0])+1) + ","
  log("changed.")
  log(texts[0])
  
# 파일 다시 쓰기
with open("index.html", "w", encoding="utf-8") as file:
    file.writelines(texts)

log("fin")
