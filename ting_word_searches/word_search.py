from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    return search_queue(word, instance, False)


def search_by_word(word, instance: Queue):
    return search_queue(word, instance, True)


def search_queue(word, instance: Queue, return_text=False):
    result = []

    # Iterate over each file in the queue
    for file in instance._queue:
        # Prepare the occurrence list for the current file
        occurrences = []

        # Iterate over each line in the file
        for line_number, linha in enumerate(
            file["linhas_do_arquivo"], start=1
        ):
            # Check for the word (case insensitive)
            if word.lower() in linha.lower():
                # Record the line number and conten (if required) where the word is found
                if return_text:
                    occurrences.append(
                        {"linha": line_number, "conteudo": linha}
                    )
                else:
                    occurrences.append({"linha": line_number})

        # If occurrences were found, add them to the result
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
