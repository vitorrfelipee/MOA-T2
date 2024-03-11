import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def heuristica_playlist():
    """
    Heurística Playlist:

    Esta heurística é baseada na ideia de criar uma playlist de músicas, onde cada música tem um valor associado
    (representando sua utilidade) e um peso associado (representando a capacidade que ela ocupa na mochila). A heurística
    ordena as músicas pela relação utilidade/peso e seleciona as músicas mais "valiosas" até que a capacidade máxima da
    mochila seja atingida.
    """
    pass

def ler_dados(arquivo):
    pesos = []
    utilidades = []
    capacidade = 0
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        pesos = [int(x) for x in linhas[0].split(':')[1].split()]
        utilidades = [int(x) for x in linhas[3].split(':')[1].split()]
        capacidade = int(linhas[6].split('=')[1].strip())
    return pesos, utilidades, capacidade

def borsa(arquivo, n):
    def heuristica_mochila(pesos, utilidades, capacidade):
        n = len(pesos)
        itens_selecionados = []
        peso_total = 0
        utilidade_total = 0

        # Ordena os itens por utilidade/peso
        relacao_utilidade_peso = [(utilidades[i] / pesos[i], i) for i in range(n)]
        relacao_utilidade_peso.sort(reverse=True)

        # Adiciona itens à mochila até que a capacidade seja excedida
        for utilidade_peso, indice in relacao_utilidade_peso:
            if peso_total + pesos[indice] <= capacidade:
                itens_selecionados.append((indice, pesos[indice], utilidades[indice]))
                peso_total += pesos[indice]
                utilidade_total += utilidades[indice]

        return itens_selecionados, peso_total, utilidade_total

    # Lendo os dados do arquivo
    pesos, utilidades, capacidade = ler_dados(arquivo)

    # Aplicando a heurística para o problema da mochila
    itens_selecionados, peso_maximo_carregado, utilidade_total = heuristica_mochila(pesos, utilidades, n)

    # Escrever os resultados em um arquivo de saída
    arquivo_saida = arquivo.replace(".txt", "_results.txt")
    with open(arquivo_saida, 'w') as f:
        f.write("Heuristica Playlist:\n")
        f.write("Esta heuristica e baseada na ideia de criar uma playlist de msusicas, onde cada musica tem um valor associado\n")
        f.write("(representando sua utilidade) e um peso associado (representando a capacidade que ela ocupa na playlist). A heuristica\n")
        f.write("ordena as musicas pela relacao utilidade/peso e seleciona as musicas mais \"valiosas\" ate que a capacidade maxima da\n")
        f.write("playlist seja atingida.\n\n")
        f.write("Resultados:\n")
        f.write(f"Valor de n: {n}\n")
        f.write("Itens selecionados:\n")
        for item in itens_selecionados:
            f.write(f"Item: {item[0]}, Peso: {item[1]}, Utilidade: {item[2]}\n")
        f.write(f"Peso carregado: {peso_maximo_carregado}\n")
        f.write(f"Utilidade total: {utilidade_total}\n")

    messagebox.showinfo("Concluído", f"Os resultados foram salvos em '{arquivo_saida}'")

def selecionar_arquivo():
    arquivo_entrada = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
    if arquivo_entrada:
        try:
            pesos, utilidades, capacidade_mochila = ler_dados(arquivo_entrada)
            borsa(arquivo_entrada, capacidade_mochila)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Resolução do Problema da Mochila")

# Botão para selecionar arquivo
btn_selecionar_arquivo = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_selecionar_arquivo.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()
