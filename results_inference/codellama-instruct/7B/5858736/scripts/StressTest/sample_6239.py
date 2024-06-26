sock_pairs_premise = 10
sock_pairs_hypothesis = 20

if sock_pairs_hypothesis <= sock_pairs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
