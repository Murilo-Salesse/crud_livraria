# Projeto Django

Este repositório contém um projeto Django. Para interagir com o projeto, utilize os seguintes comandos no terminal. **Certifique-se de estar na pasta onde está localizado o arquivo `manage.py` antes de executar qualquer comando.**

## Comandos

### 1. `python manage.py makemigrations`

- **Descrição**: Este comando é usado para criar novas migrações com base nas mudanças feitas nos modelos do Django. Ele verifica se houve alterações nos modelos e gera um arquivo de migração que reflete essas mudanças.

### 2. `python manage.py migrate`

- **Descrição**: Este comando aplica as migrações pendentes ao banco de dados. Ele atualiza a estrutura do banco de dados de acordo com as migrações que foram criadas anteriormente, garantindo que a base de dados esteja em sincronia com os modelos definidos no código.

### 3. `python manage.py runserver`

- **Descrição**: Este comando inicia o servidor de desenvolvimento do Django. Após executá-lo, você poderá acessar a aplicação web através do navegador, geralmente no endereço `http://127.0.0.1:8000/`. Este servidor é ideal para desenvolvimento e testes, mas não é recomendado para uso em produção.

## Como usar

1. **Abra o terminal** e navegue até o diretório do seu projeto Django onde o arquivo `manage.py` está localizado.
   
2. Execute os comandos conforme necessário:

   - Para criar migrações:
     ```bash
     python manage.py makemigrations
     ```

   - Para aplicar as migrações ao banco de dados:
     ```bash
     python manage.py migrate
     ```

   - Para iniciar o servidor de desenvolvimento:
     ```bash
     python manage.py runserver
     ```

## Licença

Feito por Murilo Salesse
