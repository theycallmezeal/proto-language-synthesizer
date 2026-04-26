import csv
import Levenshtein
import random
import time

data = []
with open('data.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)

data = [[entry[0], entry[0], entry[1], entry[2]] for entry in data]
# input word, in-progress word, output word, meaning

def distance(data):
    return sum(Levenshtein.distance(entry[1], entry[2], weights=(2, 1, 1)) for entry in data)

# alphabet = list(set(''.join([entry[0] + entry[2] for entry in data])))

# potential_rules = set()
# for char1 in alphabet:
#     for char2 in alphabet:
#         for char3 in alphabet:
#             # a rule is a tuple of (before, after)
#             potential_rules.add((char1 + char2, char1 + char3))
#             potential_rules.add((char1 + char2, char3 + char2))
#             potential_rules.add((char1, char3))
#             potential_rules.add((char1, ''))
#             potential_rules.add((char1 + char2, char1))
#             potential_rules.add((char1 + char2, char2))

# baseline_distance = distance(data)

# good_rules = [
#     rule for rule in potential_rules
#     if distance([[entry[0], entry[1].replace(rule[0], rule[1]), entry[2], entry[3]] for entry in data]) < baseline_distance
# ]

good_rules = [('j', 'u'), ('ʊj', 'ʊw'), ('ʊb', 'ub'), ('cu', 'cf'), ('bʊ', 'by'), ('aj', 'az'), ('pa', 'ba'), ('ʊc', 'uc'), ('j', 'ɲ'), ('ki', 'k'), ('ʊt', 'ut'), ('ji', 'ki'), ('ʊ', 'w'), ('up', 'uf'), ('ʊe', 'we'), ('jɪ', 'j'), ('de', 're'), ('jʊ', 'ju'), ('dʊ', 'du'), ('ku', 'vu'), ('cu', 'c'), ('ɪm', 'im'), ('ɪk', 'ik'), ('ʊj', 'ʊk'), ('j', ''), ('ʊd', 'ʊr'), ('ʊ', 'u'), ('do', 'zo'), ('pa', 'fa'), ('dʊ', 'dw'), ('cu', 'fu'), ('tʊ', 'tw'), ('id', 'ir'), ('po', 'ho'), ('je', 'we'), ('ki', 'i'), ('ca', 'sa'), ('ge', 'gi'), ('ge', 'ʒe'), ('ɪj', 'j'), ('kɪ', 'ki'), ('uɪ', 'ɪ'), ('ʊe', 'ue'), ('ad', 'ar'), ('do', 'ro'), ('ti', 'si'), ('ji', 'ʒi'), ('bu', 'vu'), ('ʊn', 'on'), ('j', 'i'), ('gʊ', 'gw'), ('ʊj', 'ʊu'), ('ic', 'if'), ('ed', 'er'), ('c', 'š'), ('ʊj', 'j'), ('jɪ', 'iɪ'), ('gu', 'vu'), ('c', 's'), ('ki', 'kć'), ('ap', 'ah'), ('ʊa', 'wa'), ('ɪj', 'ɪć'), ('cu', 'ci'), ('ce', 'se'), ('kʊ', 'ku'), ('ʊd', 'ud'), ('ʊc', 'ʊs'), ('cu', 'u'), ('ɪg', 'ig'), ('pa', 'ha'), ('jɪ', 'zɪ'), ('c', 'ʃ'), ('jʊ', 'oʊ'), ('ɪd', 'id'), ('ʊj', 'ʊ'), ('bʊ', 'bw'), ('ac', 'as'), ('di', 'zi'), ('ʊn', 'un'), ('ʊi', 'wi'), ('nɲ', 'ɲ'), ('jʊ', 'ɲʊ'), ('ʊg', 'ug'), ('ɪt', 't'), ('ja', 'a'), ('od', 'or'), ('da', 'ra'), ('ic', 'iš'), ('tʊ', 'tu'), ('jɪ', 'ji'), ('gɪ', 'gi'), ('nj', 'nɲ'), ('ji', 'ui'), ('ʊ', 'y'), ('ɪd', 'ɪr'), ('jo', 'zo'), ('ɪ', 'ɟ'), ('p', 'b'), ('c', 'f'), ('ia', 'ya'), ('ji', 'zi'), ('ji', 'wi'), ('ci', 'ʃi'), ('ʊj', 'ʊi'), ('ai', 'a'), ('dɪ', 'dy'), ('mʊ', 'mu'), ('ʊj', 'wj'), ('ag', 'ab'), ('p', 'h'), ('ɪj', 'ćj'), ('d', 'z'), ('uɪ', 'iɪ'), ('kʊ', 'kw'), ('gɪ', 'gɟ'), ('tu', 'ču'), ('gu', 'mu'), ('ɪb', 'ib'), ('ji', 'i'), ('jʊ', 'jo'), ('up', 'uw'), ('ʊm', 'um'), ('cʊ', 'cw'), ('d', 'r'), ('cʊ', 'sʊ'), ('ji', 'ii'), ('ɪ', 'i'), ('j', 'z'), ('ʊj', 'uj'), ('ɪt', 'it'), ('un', 'u'), ('ed', 'ez'), ('ku', 'gu'), ('ʊk', 'uk'), ('dɪ', 'di'), ('ʊe', 'ye'), ('ud', 'ur'), ('uɪ', 'u'), ('tɪ', 'ti'), ('ij', 'iz'), ('pa', 'wa'), ('jo', 'wo'), ('ku', 'pu'), ('co', 'so'), ('mʊ', 'mw'), ('ɪ', 'y'), ('ip', 'ib'), ('jo', 'o'), ('ja', 'wa'), ('oi', 'oe'), ('uɪ', 'ui'), ('dʊ', 'rʊ'), ('ki', 'ći'), ('ʊ', 'o'), ('eg', 'ig'), ('jʊ', 'zʊ'), ('ja', 'za'), ('ap', 'ab'), ('dɪ', 'rɪ'), ('ip', 'ih'), ('gi', 'zi'), ('kɪ', 'kć'), ('gʊ', 'gu'), ('ɪ', 'ć'), ('j', 'w'), ('uɪ', 'fɪ'), ('nʊ', 'nw'), ('bi', 'by'), ('ti', 'ci'), ('di', 'ri'), ('ɪj', 'ɪ'), ('mo', 'mw'), ('je', 'e'), ('oi', 'wi'), ('co', 'šo'), ('nj', 'nz'), ('bʊ', 'bu'), ('jɪ', 'ɪ')]

print(distance(data))

# ATTEMPTS = 100
# best_program = []
# best_score = 10000000
# for i in range(ATTEMPTS):
#     if i % 100 == 0:
#         print('.', end='', flush=True)
#     attempt_data = data.copy()
#     rules = good_rules.copy()
#     random.shuffle(rules)
#     program = []
#     score_to_beat = distance(data)
#     for rule in rules:
#         data_after_rule = [[entry[0], entry[1].replace(rule[0], rule[1]), entry[2], entry[3]] for entry in attempt_data]
#         score_after_rule = distance(data_after_rule)
#         if score_after_rule < score_to_beat:
#             program.append(rule)
#             attempt_data = data_after_rule
#             score_to_beat = score_after_rule
#     if score_to_beat < best_score:
#         best_program = program
#         best_score = score_to_beat
#         print(best_score)
#     if best_score == 0:
#         break

# print(best_program, best_score)
# for rule in best_program:
#     data = [[entry[0], entry[1].replace(rule[0], rule[1]), entry[2], entry[3]] for entry in data]
# print(data)
