from jsonpath_ng import parse


def search_created_pet_in(pets, status):
    return [pet for pet in pets if pet['status'] == pet][0]


def search_nodes_using_json_path(pets, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(pets)]
