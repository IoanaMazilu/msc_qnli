sock_pairs_premise = 15
sock_pairs_hypothesis = 75

if sock_pairs_hypothesis <= sock_pairs_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
