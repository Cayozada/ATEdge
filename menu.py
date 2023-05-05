import searcher

class Menu:
    def __init__(self):
        print("""
        ____  _             _         ____               _         _    _
       / ___|| |__    __ _ (_) _ __  / ___|   ___  _ __ (_) _ __  | |_ (_) _ __    __ _
      | |    | '_ \  / _` || || '_ \ \___ \  / __|| '__|| || '_ \ | __|| || '_ \  / _` |
      | |___ | | | || (_| || || | | | ___) || (__ | |   | || |_) || |_ | || | | || (_| |
       \____||_| |_| \__,_||_||_| |_||____/  \___||_|   |_|| .__/  \__||_||_| |_| \__, |
                                                        |_||_|                    |___/
          _     _____    _____      _                ____               _         _
         / \   |_   _|  | ____|  __| |  __ _   ___  / ___|   ___  _ __ (_) _ __  | |_
        / _ \    | |    |  _|   / _` | / _` | / _ \ \___ \  / __|| '__|| || '_ \ | __|
       / ___ \   | |    | |___ | (_| || (_| ||  __/  ___) || (__ | |   | || |_) || |_
      /_/   \_\  |_|    |_____| \__,_| \__, | \___| |____/  \___||_|   |_|| .__/  \__|
                                        |___/                             |_| 
        """)
        print("""
        ╔════════════════════════════════════════╗
        ║       Bem-vindo ao ATedgeScript!       ║
        ║                                        ║
        ║   Digite [E] para Executar.            ║
        ║                                        ║
        ║   Digite [Q] para Sair                 ║
        ║                                        ║
        ╚════════════════════════════════════════╝ 
        """)

    def select_option(self, option):
        if(option == "e"):
            searcher.searcher_main()
        elif(option == "q"):
            raise SystemExit

    def run(self):
        script_selected = input("[INPUT]: Aguardando Comando: ").lower()
        self.select_option(script_selected)
    
    def menu(self):
        while True:
            self.run()  

if __name__ == "__main__":
    menu = Menu()
    menu.menu()