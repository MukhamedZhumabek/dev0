import hashlib
from typing import Mapping


def check_sum(data: Mapping[str, str]) -> bool:
    """
    :param data: {data: string, control_sum: string}
    :return: equal hashfunction(data) and control_sum
    """
    h = hashlib.sha256()
    h.update(data['data'].encode('utf-8'))
    return h.hexdigest() == data['control_sum']
