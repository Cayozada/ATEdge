from selenium.webdriver.edge.service import Service
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import urllib.request
import traceback
import zipfile
import random
import psutil
import time
import os

class BingSearcher:
    def __init__(self):
        self.webdriver_path = self._set_webdriver_path()
        self.search_number = self._get_search_number()
        self.driver = None

    def _get_default_path(self):
        return os.path.join(os.path.expanduser("~"), "Documents", "msWebDriver")

    def _get_full_default_path(self):
        return f"{self._get_default_path()}\\msedgedriver.exe" 
    
    def show_loading_animation(self, message, duration, fps=10):
        animation_chars = ['-', '\\', '|', '/']  
        total_frames = duration * fps 
        current_frame = 0  
        start_time = time.time()  
        while current_frame < total_frames:
            current_char_index = current_frame % len(animation_chars)  
            print(f"{message} {animation_chars[current_char_index]}", end='\r')  
            time_left = duration - (time.time() - start_time)
            time_per_frame = time_left / (total_frames - current_frame)
            time.sleep(time_per_frame)  
            current_frame += 1 
        print(f"{message}, concluído!")
    
    def script_info(self, info, level):
        if(level == 0):
            return f"[INFO]: {info}"
        elif(level == 1):
            return input(f"[INPUT]: {info}").lower()
        elif(level == 2):
            return f"[ERROR]: {info}"

    def _catch_edge_version(self):
        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--remote-debugging-port=9222")
        driver = Edge(options=options)
        edge_version = driver.capabilities['browserVersion']
        return edge_version
    
    def _make_download(self, edge_version):
        os.makedirs(self._get_default_path(), exist_ok=True)
        url = f"https://msedgedriver.azureedge.net/{edge_version}/edgedriver_win32.zip"
        urllib.request.urlretrieve(url, os.path.join(self._get_default_path(), "edgedriver_win32.zip"))
        return os.path.join(self._get_default_path(), "edgedriver_win32.zip")
    
    def _extract_last_version(self, zip_path, default_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(default_path)

    def _make_path_webdriver(self):
        print(self.script_info("O caminho padrão do webdriver não foi encontrado, irei criá-lo para voce :)", 0))
        print(self.script_info("Aguarde!", 0))
        zip_path = self._make_download(self._catch_edge_version())
        self.show_loading_animation(self.script_info("Baixando a última versão do webdriver", 0), 4)
        self.show_loading_animation(self.script_info("Extraindo", 0), 4)
        self._extract_last_version(zip_path, self._get_default_path())
        os.remove(zip_path)
    
    def _verify_webdriver_path(self, path_webdriver):
        self.show_loading_animation(self.script_info("Procurando webdriver", 0), 4)
        if not os.path.exists(path_webdriver):
            self._make_path_webdriver()
            return path_webdriver
        elif os.path.exists(path_webdriver):
            print(self.script_info("O caminho padrão foi encontrado!", 0))
            return path_webdriver

    def _set_webdriver_path(self):
        return self._verify_webdriver_path(self._get_full_default_path())

    def _set_edge_options(self):
        user_dir = os.getenv("USERPROFILE")
        edge_options = EdgeOptions()
        edge_options.add_argument(f"user-data-dir={user_dir}\\AppData\\Local\\Microsoft\\Edge\\User Data")
        edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        edge_options.add_argument("--start-maximized")
        return edge_options

    def _check_and_close_edge_instances(self):
        edge_processes = [p for p in psutil.process_iter() if 'msedge.exe' in p.name()]
        if edge_processes:
            for process in edge_processes:
                process.kill()
            self.show_loading_animation(self.script_info("Fechando instâncias do Microsoft Edge em andamento", 0), 4)
            print(self.script_info("Instâncias do Microsoft Edge em execução fechadas com sucesso.", 0))
        else:
            self.show_loading_animation(self.script_info("Não foram encontradas instâncias do Microsoft Edge em execução, prosseguindo", 0), 6)
            print(self.script_info("Aguarde!", 0))

    def _treat_instance_error(self):
        command = self.script_info("Digite [R] para atualizar o webdriver e [Q] para sair: ", 1)
        if(command == "q"):
            raise SystemExit
        if(command == "r"):
            os.remove(self._get_full_default_path())
            searcher_main() 

    def _edge_instance(self):
        self._check_and_close_edge_instances()
        try:
            edge_driver_path = Service(f"{self.webdriver_path}")
            self.driver = Edge(service=edge_driver_path, options=self._set_edge_options())
        except Exception as e:
            print(self.script_info("Houve um erro ao instanciar O Edge webdriver", 2))
            print(self.script_info("A versão do webdriver pode estar incompatível!!", 0))
            print(self.script_info("Veja o log para mais informações", 0))
            with open('error_log.txt', 'w') as f:
                f.write(str(e) + '\n')
                traceback.print_exc(file=f)
            self._treat_instance_error()

    def _get_search_number(self):
        search_option = self.script_info("Deseja inserir o número de pesquisas? [S]-sim / [N]-não: ", 1)
        if(search_option == "s"):
            while True:
                try:
                    search_number = int(self.script_info("Digite o número de pesquisas que deseja realizar: ", 1))
                    if search_number > 0:
                        return search_number
                    else:
                        self.script_info("Número inválido, digite um número maior que 0.", 0)
                except ValueError:
                    self.script_info("Entrada inválida, digite um número inteiro maior que 0.", 0)
        elif(search_option == "n"):
            self.script_info("Usarei o valor padrão (50 pesquisas)!", 0)
            search_number = 50
            return search_number
                
    def _search_bing(self, search_term):
        self.driver.get("https://www.bing.com/") 
        search_box = self.driver.find_element("name", "q") 
        search_box.send_keys(search_term)
        time.sleep(3)
        search_box.send_keys(Keys.RETURN)

    def _init_searches(self):
        self.script_info("Iniciando Pesquisas, Aguarde", 0)
        for search in tqdm(range(self.search_number), desc="[INFO]: Progresso"): 
            search_term = str(random.randint(1, 100))
            self._search_bing(search_term)
        print(self.script_info("Pesquisas concluidas!", 0))
        print(self.script_info("Aguarde!", 0))

    def run(self):
        if self.webdriver_path:
            self._edge_instance()
            if self.driver:
                self._init_searches()
                self.driver.quit()

def searcher_main():
    bing_searcher = BingSearcher()
    bing_searcher.run()

if __name__ == "__main__":
    searcher_main()