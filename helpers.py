from typing import Any, Dict, List


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items = []
    for key, value in nested_dict.items():
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def get_unique_elements(elements: List[Any]) -> List[Any]:
    return list(set(elements))


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def parse_query_string(query: str) -> Dict[str, List[str]]:
    if not query:
        return {}
    return {k: v.split(',') for k, v in (param.split('=') for param in query.split('&'))}
