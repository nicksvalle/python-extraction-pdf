# PDF Clause Extractor

This project was developed during my internship at LMP Certificações. The goal of the project is to extract clauses from tables in PDF files that contain the value "N/A" in the last column, starting from a specified page. The extracted clauses are saved in an Excel file for easy analysis.

## Features

- Reads PDF files using the `pdfplumber` library.
- Extracts tables from a specific page.
- Checks and extracts clauses containing "N/A" in the last column.
- Saves the extracted clauses into an Excel file with separate tabs for each page.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-clause-extractor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pdf-clause-extractor
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place the PDF file you want to analyze in the project directory.

2. Update the file path in the code (`pdf_path`).

3. Run the script:
   ```bash
   python extract_clauses.py
   ```

4. The results will be saved in an Excel file named `clauses_with_na.xlsx` in the project directory.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Credits

Developed by **Nicolas de Oliveira Valle** during an internship at **LMP Certificações**.

## Contact

For further inquiries, here are my contacts:

- LinkedIn: [www.linkedin.com/in/nicolas-valle-620b29219](https://www.linkedin.com/in/nicolas-valle-620b29219)
- Instagram: [www.instagram.com/nicks.valle/](https://www.instagram.com/nicks.valle/)
- Email: nicolasdeoliveiravalle@gmail.com

# PDF Clause Extractor

Este projeto foi desenvolvido durante meu estágio na LMP Certificações. O objetivo do projeto é extrair cláusulas de tabelas em arquivos PDF que contêm o valor "N/A" na última coluna, a partir de uma página especificada. As cláusulas extraídas são salvas em um arquivo Excel para fácil análise.

## Funcionalidades

- Leitura de arquivos PDF usando a biblioteca `pdfplumber`.
- Extração de tabelas a partir de uma página específica.
- Verificação e extração de cláusulas que contêm "N/A" na última coluna.
- Salvamento das cláusulas extraídas em um arquivo Excel com abas separadas para cada página.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/pdf-clause-extractor.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd pdf-clause-extractor
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque o arquivo PDF que deseja analisar no diretório do projeto.
2. Atualize o caminho do arquivo PDF no código (`pdf_path`).
3. Execute o script:
    ```bash
    python extract_clauses.py
    ```
4. Os resultados serão salvos em um arquivo Excel chamado `clauses_with_na.xlsx` no diretório do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## Créditos

Desenvolvido por Nicolas de Oliveira Valle durante estágio na LMP Certificações.

## Contato
Para mais dúvidas, segue abaixo minhas redes:
Linkedin: www.linkedin.com/in/nicolas-valle-620b29219
Instagram: www.instagram.com/nicks.valle/
Email: nicolasdeoliveiravalle@gmail.com


