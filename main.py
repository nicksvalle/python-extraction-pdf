import pdfplumber
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def process_pdf(pdf_path, output_path):
    tables_with_na = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(len(pdf.pages)):
            if page_num < 9:
                continue
            page = pdf.pages[page_num]

            table = page.extract_table()

            if table:
                df = pd.DataFrame(table[1:], columns=table[0])

                df.iloc[:, -1] = df.iloc[:, -1].fillna('')

                if df.iloc[:, -1].str.contains("N/A", na=False).any():
                    clauses_with_na = df[df.iloc[:, -1].str.contains("N/A", na=False)].iloc[:, 0].tolist()
                    tables_with_na.append({
                        "page": page_num + 1,
                        "clauses": clauses_with_na,
                        "dataframe": df[df.iloc[:, -1].str.contains("N/A", na=False)]
                    })

    if tables_with_na:
        with pd.ExcelWriter(output_path) as writer:
            for table in tables_with_na:
                sheet_name = f'Page_{table["page"]}'
                table["dataframe"].to_excel(writer, sheet_name=sheet_name, index=False)
        messagebox.showinfo("Sucesso", f"Resultados salvos em {output_path}")
    else:
        messagebox.showinfo("Aviso", "Nenhuma tabela com 'N/A' encontrada para exportar.")

def select_file():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if output_path:
            process_pdf(pdf_path, output_path)

root = tk.Tk()
root.title("Extrator de Cláusulas com 'N/A'")

select_button = tk.Button(root, text="Selecionar PDF", command=select_file)
select_button.pack(pady=20)

root.mainloop()
