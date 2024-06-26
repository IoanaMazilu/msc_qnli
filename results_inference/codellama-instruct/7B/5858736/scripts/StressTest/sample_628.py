sock_pairs_premise = 70
sock_pairs_hypothesis = 10

if sock_pairs_hypothesis >= sock_pairs_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
