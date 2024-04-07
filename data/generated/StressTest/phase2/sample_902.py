# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of less than 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: contradiction

outfit_shirt_premise = 1
outfit_shirt_hypothesis = 1
outfit_jeans_premise = 1
outfit_jeans_hypothesis = 1
outfit_sneakers_premise = 1
outfit_sneakers_hypothesis = 1

# the hypothesis refers to the number of shirts, jeans, and sneakers in an outfit mentioned in the premise
if outfit_shirt_hypothesis > outfit_shirt_premise:
    # check if the number of shirts in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif outfit_jeans_hypothesis > outfit_jeans_premise:
    # check if the number of jeans in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif outfit_sneakers_hypothesis > outfit_sneakers_premise:
    # check if the number of sneakers in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

