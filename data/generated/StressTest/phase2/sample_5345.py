# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 4 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: contradiction

shirt_premise = 1
shirt_hypothesis = 4
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis refers to the number of shirts, jeans, and sneakers mentioned in the premise
if shirt_premise != shirt_hypothesis:
    # check if the hypothesis value contradicts the number of shirts in the premise
    label = "contradiction"
elif jeans_premise != jeans_hypothesis:
    # check if the number of jeans in the hypothesis contradicts the number of jeans in the premise
    label = "contradiction"
elif sneakers_premise != sneakers_hypothesis:
    # check if the number of sneakers in the hypothesis contradicts the number of sneakers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

