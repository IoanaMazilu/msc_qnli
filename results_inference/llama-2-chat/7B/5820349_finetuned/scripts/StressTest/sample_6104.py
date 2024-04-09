babysitting_start_age_premise = 18
babysitting_start_age_hypothesis = 58

# the hypothesis refers to the age Jane started babysitting, also mentioned in the premise
if babysitting_start_age_hypothesis!= babysitting_start_age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
