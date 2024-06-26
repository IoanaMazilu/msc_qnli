shirt_premise = 1
shirt_hypothesis = 3
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis and the premise talk about the composition of an outfit
# we compare the number of shirts, jeans, and sneakers in the hypothesis with the ones in the premise
if shirt_premise != shirt_hypothesis or jeans_premise != jeans_hypothesis or sneakers_premise != sneakers_hypothesis:
    # if the number of shirts, jeans, or sneakers in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the numbers in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
