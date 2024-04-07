# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of less than 2 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: entailment

outfit_shirts_premise = 1
outfit_shirts_hypothesis = 2

# the hypothesis refers to the number of shirts in an outfit, which is also mentioned in the premise
if outfit_shirts_hypothesis <= outfit_shirts_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

