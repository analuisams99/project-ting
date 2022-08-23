def exists_word(word, instance):
    output = []

    file_lines = instance._queue[0]["linhas_do_arquivo"]
    file_path = instance._queue[0]["nome_do_arquivo"]

    occurrences = [
        {"linha": index}
        for index, line in enumerate(file_lines, 1)
        if word.lower() in line.lower()
    ]

    if occurrences:
        output = [
            {
                "palavra": word,
                "arquivo": file_path,
                "ocorrencias": occurrences,
            }
        ]

    return output


def search_by_word(word, instance):
    output = []

    file_lines = instance._queue[0]["linhas_do_arquivo"]
    file_path = instance._queue[0]["nome_do_arquivo"]

    occurrences = [
        {"linha": line_index, "conteudo": line}
        for line_index, line in enumerate(file_lines, 1)
        if word.lower() in line.lower()
    ]

    if occurrences:
        output = [
            {
                "palavra": word,
                "arquivo": file_path,
                "ocorrencias": occurrences,
            }
        ]

    return output
