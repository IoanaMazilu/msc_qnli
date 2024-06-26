shirt_premise = 1
shirt_hypothesis = 7
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the same person and items of clothing as the premise
if shirt_hypothesis != shirt_premise or jeans_hypothesis != jeans_premise or sneakers_hypothesis != sneakers_premise:
    # check if the number of shirts, jeans or sneakers in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the numbers match, the hypothesis is entailed by the premise
    label = "entailment"

print(label)
