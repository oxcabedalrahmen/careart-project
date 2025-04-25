import os
import shutil


def project():
    name=input("enter your name project:")
    os.makedirs("api",exist_ok=True)
    os.makedirs(f"{name}",exist_ok=True)
    os.makedirs("web",exist_ok=True)
    with open("fastapi.py","wb") as f:
        f.write(b"""from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Input(BaseModel):
    mass:str
                
@app.get("/")
def api():
  return {"mass":"hellow wored"}
    
""")
    with open("index.html","wb") as fi:
        fi.write(b"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>broject</title>
    <link rel="stylesheet" href="style.css">
    <script src="scarpt.js"></script>
</head>
<body>
    
</body>
</html>""")
    with open("style.css","wb") as file:
        file.write(b"/*code css")
        
        
    with  open("scarpt.js","wb") as filejs:
        filejs.write(b"""//    code js  //
async function api() {
    var re=await fetch("http://127.0.0.1:8000")
    var data=await re.json()
    console.log(data.mass)
}""")

    
    with open("run.bat","w") as  run :
       run.write(fr"""@echo off
cd /d %~dp0{name}\api
uvicorn fastapi:app --reload
pause
""")



########################################################
    shutil.move("run.bat", f"{name}/run.bat")
    shutil.move("scarpt.js","web/scarpt.js")
    shutil.move("style.css","web/style.css")
    shutil.move("index.html","web/index.html")
    shutil.move("fastapi.py", "api/fastapi.py")
    shutil.move("api",f"{name}/api")
    shutil.move("web",f"{name}/web")
    

x=input("enter your password:")
if x=="123b":
     project()
     
else:
    print("erore passwrd not carect")
