# Premise: If T = 5/9 * (K-32), and if T = 20, then what is the value of K?
# Hypothesis: If T = less than 5/9 * (K-32), and if T = 20, then what is the value of K?
# Golden Label: contradiction

T_premise = 20
T_hypothesis = 20
ratio_premise = 5/9
ratio_hypothesis = 5/9

# the hypothesis refers to the same calculation as the premise
if T_hypothesis != T_premise:
    # if the temperature in the hypothesis is not the same as the one in the premise, that's a contradiction
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # check if the hypothesis ratio is less than the ratio in the premise, as stated by the hypothesis
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and the hypothesis doesn't entail the premise
    label = "neutral"

print(label)

