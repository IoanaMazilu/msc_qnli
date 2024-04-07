# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of less than 5 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: entailment

shirt_premise = 1
shirt_hypothesis = 5

# the hypothesis refers to the number of shirts in an outfit mentioned in the premise
if shirt_hypothesis > shirt_premise:
    # check if the number of shirts in the hypothesis contradicts the number of shirts in the premise
    label = "contradiction"
elif shirt_hypothesis < shirt_premise:
    # check if the number of shirts in the hypothesis is less than the number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

