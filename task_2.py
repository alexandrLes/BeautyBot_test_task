from collections import defaultdict

def group_by_unique_pairs(list_version):
    count_dict = defaultdict(int)
    
    for id_version in list_version:
        id, version = id_version
        count_dict[(id, version)] += 1
    
    result = [[id, version, count] for (id, version), count in count_dict.items()]
    
    return result

list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]
result = group_by_unique_pairs(list_version)
print(result)
