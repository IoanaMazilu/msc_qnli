shirts_salman_premise = 40
shirts_ambani_premise = 40
shirts_dalmiya_premise = 40
shirts_salman_hypothesis = 80
shirts_ambani_hypothesis = 80
shirts_dalmiya_hypothesis = 80

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya
# if the hypothesis value contradicts the premise values, we can infer contradiction
if shirts_salman_hypothesis <= shirts_salman_premise or shirts_ambani_hypothesis <= shirts_ambani_premise or shirts_dalmiya_hypothesis <= shirts_dalmiya_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
