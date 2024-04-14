import sys

from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    if not (new_text := txt_importer(path_file)) or any(
        new["nome_do_arquivo"] == path_file for new in instance._queue
    ):
        return None

    new = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(new_text),
        "linhas_do_arquivo": new_text,
    }

    instance.enqueue(new)
    print(new)


def remove(instance: Queue):
    if not len(instance):
        print("Não há elementos")
        return

    removed_new = instance.dequeue()
    print(f'Arquivo {removed_new["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance: Queue, position):
    try:
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
