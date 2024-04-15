from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    return search_queue(word, instance, False)


def search_by_word(word, instance: Queue):
    return search_queue(word, instance, True)


def check_line_for_word(line, word):
    """Helper function to check if a word exists in a line."""
    return word.lower() in line.lower()


def get_occurrences_for_line(line_number, linha, word, return_text=False):
    # Helper function to generate occurrences for a line containing the word.
    occurrences = []
    if check_line_for_word(linha, word):
        if return_text:
            occurrences.append({"linha": line_number, "conteudo": linha})
        else:
            occurrences.append({"linha": line_number})
    return occurrences


def search_queue(word, instance, return_text=False):
    result = []

    for file in instance._queue:
        occurrences = []

        for line_number, linha in enumerate(
            file["linhas_do_arquivo"], start=1
        ):
            occurrences.extend(
                get_occurrences_for_line(line_number, linha, word, return_text)
            )

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
