# Premise: If an outfit consists of less than 4 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: neutral

shirt_premise = 4
shirt_hypothesis = 1
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# The hypothesis refers to the same outfit configuration as the premise, but specifies the number of shirts
if shirt_hypothesis >= shirt_premise:
    # Check if the number of shirts in the hypothesis contradicts the maximum number of shirts in the premise
    label = "contradiction"
elif jeans_hypothesis != jeans_premise or sneakers_hypothesis != sneakers_premise:
    # Check if the number of jeans or sneakers in the hypothesis contradicts the number of jeans or sneakers in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

