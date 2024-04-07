# Premise: If T = more than 4/9 * (K-32), and if T = 105, then what is the value of K?
# Hypothesis: If T = 5/9 * (K-32), and if T = 105, then what is the value of K?
# Golden Label: neutral

T_premise = 105
T_hypothesis = 105
ratio_premise = 4/9
ratio_hypothesis = 5/9

# the hypothesis refers to the same temperature T and a similar formula to calculate 'K' as the premise
if T_premise != T_hypothesis:
    # check if the temperature T in the hypothesis contradicts the temperature T in the premise
    label = "contradiction"
elif ratio_premise < ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

