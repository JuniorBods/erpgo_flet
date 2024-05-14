from flet import *

def login(page= Page):
    
    return View(
        "/login",
        appbar=AppBar(
            Text("Login", size=40),
            ElevatedButton("Entrar", icon=icons.LOGIN)
        )
    )