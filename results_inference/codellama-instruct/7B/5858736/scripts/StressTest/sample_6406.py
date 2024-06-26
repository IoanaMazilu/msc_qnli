sock_pairs_premise = 35
sock_pairs_hypothesis = 15

if sock_pairs_hypothesis >= sock_pairs_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
