FROM python:3
ADD avito_parser.py avito_parser_cli.py requirements.txt /
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "avito_parser_cli.py"]

