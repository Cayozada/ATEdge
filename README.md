![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white)
# ATEdgeScript
Script Python de pesquisas autônomas e aleatórias utilizando o **Microsoft Edge Web Driver**.
![chainsScripting](https://cdn.discordapp.com/attachments/974114124608962611/1098331859278114886/image.png "Começo do Script")

# Pré-Requisitos
- Ultima versão do Navegador Microsoft Edge.
- Windows 32 ou 64 bits.

# Branchs
- ***Main:*** código fonte aberto do Script.
- ***Build-v1:*** arquivo executavel  

# Blibliotecas Principais
- ***Selenium 4***
- ***tqdm***
- ***psutils***

o resumo completo das blibliotecas esta no arquivo **requirements.txt**.

# Instalação via fonte
execute via terminal:
```python
pip install -r requirements.txt
```

# Execução
ao encontrar ou criar o caminho padrão para o webdriver e fechar instancias existentes do Microsoft Edge, uma vez que possam atrapalhar o processo de execução do webdriver, o usuário pode escolher se deseja inserir o número de pesquisas, e caso não, será utilizado o valor padrão de 50 pesquisas, apos a realização das pesquisas, pode se escolher entre reiniciar e sair.

# Ideias Futuras
- ***Suporte para multiplataforma (MAC OS, Linux)***

**OBS:** Esse Script foi feito com o intuito de farmar pontos de pesquisa do Microsoft Rewards de forma automática, porém sinta-se à vontade para utilizá-lo de outra maneira.
