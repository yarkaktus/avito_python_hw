from collections import defaultdict
from math import ceil
from typing import Iterable, Optional, List, Tuple, Any, Dict


# - делать все на функциях
# - должно работать со всеми Iterable: списки, генераторы, проч.
# - по возможности возвращать генератор (ленивый объект)
# - тесты на pytest + pytest-doctest, покрыть как можно больше кейсов
# - в помощь: itertools, collections, funcy, google


# 1. Написать функцию получения размера генератора
def ilen(iterable: Iterable) -> int:
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for _ in iterable)


# 2. Написать функцию flatten, которая из многоуровневого массива сделает одноуровневый

def flatten(iterable: Iterable) -> Iterable:
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    result = []
    for elem in iterable:
        if isinstance(elem, Iterable):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result


# 3. Написать функцию, которая удалит дубликаты, сохранив порядок
def distinct(iterable: Iterable) -> List[Any]:
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    result = []
    for elem in iterable:
        if elem not in result:
            result.append(elem)
    return result


# 4. Неупорядоченная последовательность из словарей, сгруппировать по ключу, на выходе словарь
def groupby(key, iterable: Iterable) -> Dict:
    result = defaultdict(list)

    for elem in iterable:
        value = elem[key]
        result[value].append(elem)

    return dict(result)


# 5. Написать функцию, которая разобьет последовательность на заданные куски
def chunks(size: int, iterable: Iterable) -> Optional[List[Tuple]]:
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4)]
    """
    result = []
    iterable_list = list(iterable)
    chunk_count = ceil(len(iterable_list) / size)
    for chunk_num in range(chunk_count):
        left = chunk_num * size
        right = (chunk_num + 1) * size
        result.append(tuple(iterable_list[left:right]))
    return result


# 6. Написать функцию получения первого элемента или None
def first(iterable: Iterable) -> Any:
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0)) is None
    True
    """
    try:
        return next(iter(iterable))
    except Exception:
        return None


# 7. Написать функцию получения последнего элемента или None
def last(iterable: Iterable) -> Any:
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0)) is None
    True
    """
    try:
        return list(iterable)[-1]
    except Exception:
        return None
