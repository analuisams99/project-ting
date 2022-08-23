import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    for item in range(len(instance)):
        if path_file in instance.search(item)["nome_do_arquivo"]:
            return None

    instance.enqueue(output)
    print(output)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")

    else:
        file_name = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))

    except IndexError:
        print("Posição inválida", file=sys.stderr)
