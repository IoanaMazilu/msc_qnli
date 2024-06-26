boys_age_14_premise = 80
boys_age_14_hypothesis = 50
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis refers to the number of boys of each age mentioned in the premise
if boys_age_14_hypothesis!= boys_age_14_premise or boys_age_15_hypothesis!= boys_age_15_premise or boys_age_13_hypothesis!= boys_age_13_premise or boys_age_12_hypothesis!= boys_age_12_premise:
    # check if the number of boys of each age in the hypothesis contradicts the number of boys of each age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
