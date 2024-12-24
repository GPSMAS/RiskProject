import subprocess

def execute_notebook(notebook_path):
    """
    Esegue un notebook Jupyter utilizzando nbconvert.
    """
    command = [
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        notebook_path
    ]
    subprocess.run(command, check=True)
    print(f"Notebook {notebook_path} eseguito con successo!")

def main():
    # Elenco dei notebook da eseguire in ordine
    notebooks = [
        "1_Create_df_lav1_v5_.ipynb",
        "2_Lav_1_work_3.3-LR_W.ipynb",
        "3_Lav_1_work_3.3-RF_W.ipynb",
        "4_Lav_1_work_3.3-Esemble_stacking_W.ipynb",
        "5_Lav_1_work_3.3-Esemble_voting_W.ipynb",
        "6_Model_Result_Comparison.ipynb"
    ]
    
    print("Ecco l'elenco dei notebook disponibili:")
    for idx, notebook in enumerate(notebooks, 1):
        print(f"{idx}. {notebook}")
    
    while True:
        try:
            start_index = int(input("Inserisci il numero del notebook da cui partire (1-6): ")) - 1
            if 0 <= start_index < len(notebooks):
                break
            else:
                print("Per favore, inserisci un numero valido tra 1 e 6.")
        except ValueError:
            print("Input non valido. Inserisci un numero tra 1 e 6.")
    
    for i in range(start_index, len(notebooks)):
        notebook = notebooks[i]
        print(f"Pronto per eseguire il notebook: {notebook}")
        user_input = input("Vuoi eseguire questo notebook? (s/n): ").strip().lower()
        if user_input == "s":
            execute_notebook(notebook)
        else:
            print(f"Esecuzione interrotta. Il notebook {notebook} non è stato eseguito.")
            break

    print("Flusso completato (o interrotto) con successo!")

if __name__ == "__main__":
    main()
