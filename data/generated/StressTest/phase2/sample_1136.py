# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 5 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: contradiction

shirt_premise = 1
jeans_premise = 1
sneakers_premise = 1

shirt_hypothesis = 5
jeans_hypothesis = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of different outfits Jordan can have with a different number of shirts than the premise
if shirt_hypothesis != shirt_premise or jeans_hypothesis != jeans_premise or sneakers_hypothesis != sneakers_premise:
    # check if the number of shirts, jeans or sneakers in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
