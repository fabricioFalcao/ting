from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
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
                # Record the line number where the word is found
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


def search_by_word(word, instance: Queue):
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
                # Record the line number where the word is found
                occurrences.append({"linha": line_number, "conteudo": linha})

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
