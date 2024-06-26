sock_pairs_premise = 13
sock_pairs_hypothesis = 83

if sock_pairs_hypothesis <= sock_pairs_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
