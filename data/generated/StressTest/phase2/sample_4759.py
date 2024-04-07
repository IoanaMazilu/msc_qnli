# Premise: If an outfit consists of less than 5 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: neutral

shirts_premise = 5
shirts_hypothesis = 1
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the same type of outfit as the premise
if shirts_hypothesis >= shirts_premise:
    # check if the number of shirts in the hypothesis contradicts the premise
    label = "contradiction"
elif jeans_hypothesis != jeans_premise or sneakers_hypothesis != sneakers_premise:
    # check if the number of jeans or sneakers in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

