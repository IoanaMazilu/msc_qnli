# Premise: The ages of Nishi and vinnee are in the ratio of less than 7:5 respectively.
# Hypothesis: The ages of Nishi and vinnee are in the ratio of 6:5 respectively.
# Golden Label: neutral

ratio_premise = 7/5
ratio_hypothesis = 6/5

# the hypothesis refers to the age ratio of Nishi and Vinnee mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the age ratio in the hypothesis contradicts the 'less than' estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

