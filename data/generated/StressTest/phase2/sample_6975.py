# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of less than 8 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: entailment

outfit_shirt_premise = 1
outfit_shirt_hypothesis = 8
outfit_jeans_premise = 1
outfit_jeans_hypothesis = 1
outfit_sneakers_premise = 1
outfit_sneakers_hypothesis = 1

# The hypothesis refers to the number of shirts, jeans and sneakers mentioned in the premise
if outfit_shirt_premise >= outfit_shirt_hypothesis:
    # Check if the estimate of 'outfit_shirt_hypothesis' contradicts the number of shirts in the premise
    label = "contradiction"
elif outfit_jeans_hypothesis != outfit_jeans_premise or outfit_sneakers_hypothesis != outfit_sneakers_premise:
    # Check if the number of jeans or sneakers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

