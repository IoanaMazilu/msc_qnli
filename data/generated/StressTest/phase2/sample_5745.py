# Premise: The ages of Nishi and vinnee are in the ratio of 6:5 respectively.
# Hypothesis: The ages of Nishi and vinnee are in the ratio of less than 7:5 respectively.
# Golden Label: entailment

nishi_vinnee_ratio_premise = 6/5
nishi_vinnee_ratio_hypothesis = 7/5

# the hypothesis refers to the age ratio between Nishi and vinnee mentioned in the premise
if nishi_vinnee_ratio_hypothesis <= nishi_vinnee_ratio_premise:
    # check if the 'nishi_vinnee_ratio_hypothesis' contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

