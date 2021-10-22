def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    #print([w for item in doc_list for w in item.split()])
    return list(set([doc_list.index(item) for item in doc_list for w in item.split() if keyword.lower() == w.lower().rstrip(',.')]))
    #help(str)
