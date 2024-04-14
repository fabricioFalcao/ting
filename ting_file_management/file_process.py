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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
