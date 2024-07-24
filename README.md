# PDF Clause Extractor

Este projeto foi desenvolvido durante meu estágio na [Nome da Empresa]. O objetivo do projeto é extrair cláusulas de tabelas em arquivos PDF que contêm o valor "N/A" na última coluna, a partir de uma página especificada. As cláusulas extraídas são salvas em um arquivo Excel para fácil análise.

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

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Créditos

Desenvolvido por [Nicolas de Oliveira Valle] durante estágio na [LMP Certificações].
