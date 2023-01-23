qm9_with_h = {
    'name': 'qm9',
    'atom_encoder': {'H': 0, 'C': 1, 'N': 2, 'O': 3, 'F': 4},
    'atom_decoder': ['H', 'C', 'N', 'O', 'F'],
    'charge2idx': {1: 0, 6: 1, 7: 2, 8: 3, 9: 4},
    'n_nodes': {22: 3393, 17: 13025, 23: 4848, 21: 9970, 19: 13832, 20: 9482, 16: 10644, 13: 3060,
                15: 7796, 25: 1506, 18: 13364, 12: 1689, 11: 807, 24: 539, 14: 5136, 26: 48, 7: 16, 10: 362,
                8: 49, 9: 124, 27: 266, 4: 4, 29: 25, 6: 9, 5: 5, 3: 1},
    'max_n_nodes': 29,
    'atom_types': {1: 635559, 2: 101476, 0: 923537, 3: 140202, 4: 2323},
    'distances': [903054, 307308, 111994, 57474, 40384, 29170, 47152, 414344, 2202212, 573726,
                  1490786, 2970978, 756818, 969276, 489242, 1265402, 4587994, 3187130, 2454868, 2647422,
                  2098884,
                  2001974, 1625206, 1754172, 1620830, 1710042, 2133746, 1852492, 1415318, 1421064, 1223156,
                  1322256,
                  1380656, 1239244, 1084358, 981076, 896904, 762008, 659298, 604676, 523580, 437464, 413974,
                  352372,
                  291886, 271948, 231328, 188484, 160026, 136322, 117850, 103546, 87192, 76562, 61840,
                  49666, 43100,
                  33876, 26686, 22402, 18358, 15518, 13600, 12128, 9480, 7458, 5088, 4726, 3696, 3362, 3396,
                  2484,
                  1988, 1490, 984, 734, 600, 456, 482, 378, 362, 168, 124, 94, 88, 52, 44, 40, 18, 16, 8, 6,
                  2,
                  0, 0, 0, 0,
                  0,
                  0, 0],
    'colors_dic': ['#FFFFFF99', 'C7', 'C0', 'C3', 'C1'],
    'radius_dic': [0.46, 0.77, 0.77, 0.77, 0.77],
    'with_h': True}
    # 'bond1_radius': {'H': 31, 'C': 76, 'N': 71, 'O': 66, 'F': 57},
    # 'bond1_stdv': {'H': 5, 'C': 2, 'N': 2, 'O': 2, 'F': 3},
    # 'bond2_radius': {'H': -1000, 'C': 67, 'N': 60, 'O': 57, 'F': 59},
    # 'bond3_radius': {'H': -1000, 'C': 60, 'N': 54, 'O': 53, 'F': 53}}

qm9_without_h = {
    'name': 'qm9',
    'atom_encoder': {'C': 0, 'N': 1, 'O': 2, 'F': 3},
    'atom_decoder': ['C', 'N', 'O', 'F'],
    'charge2idx': {6: 0, 7: 1, 8: 2, 9: 3},
    'max_n_nodes': 29,
    'n_nodes': {9: 83366, 8: 13625, 7: 2404, 6: 475, 5: 91, 4: 25, 3: 7, 1: 2, 2: 5},
    'atom_types': {0: 635559, 2: 140202, 1: 101476, 3: 2323},
    'distances': [594, 1232, 3706, 4736, 5478, 9156, 8762, 13260, 45674, 174676, 469292,
                    1182942, 126722, 25768, 28532, 51696, 232014, 299916, 686590, 677506,
                    379264, 162794, 158732, 156404, 161742, 156486, 236176, 310918, 245558,
                    164688, 98830, 81786, 89318, 91104, 92788, 83772, 81572, 85032, 56296,
                    32930, 22640, 24124, 24010, 22120, 19730, 21968, 18176, 12576, 8224,
                    6772,
                    3906, 4416, 4306, 4110, 3700, 3592, 3134, 2268, 774, 674, 514, 594, 622,
                    672, 642, 472, 300, 170, 104, 48, 54, 78, 78, 56, 48, 36, 26, 4, 2, 4,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'colors_dic': ['C7', 'C0', 'C3', 'C1'],
    'radius_dic': [0.77, 0.77, 0.77, 0.77],
    'with_h': False}
    # 'bond1_radius': {'C': 76, 'N': 71, 'O': 66, 'F': 57},
    # 'bond1_stdv': {'C': 2, 'N': 2, 'O': 2, 'F': 3},
    # 'bond2_radius': {'C': 67, 'N': 60, 'O': 57, 'F': 59},
    # 'bond3_radius': {'C': 60, 'N': 54, 'O': 53, 'F': 53}}

def get_dataset_info(dataset_name, remove_h):
    if dataset_name == 'qm9':
        if not remove_h:
            return qm9_with_h
        else:
            return qm9_without_h
    else:
        raise Exception("Wrong dataset %s" % dataset_name)
