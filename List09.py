def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    if i < len(list1) - 1:
        if list1[i] != list1[i + 1]:
            return False
        i += 1
    return True