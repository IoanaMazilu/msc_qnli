jane_age_premise = 20
jane_age_hypothesis = 40

# the hypothesis refers to Jane's age when she started babysitting, which is also mentioned in the premise
if jane_age_hypothesis!= jane_age_premise:
    # check if Jane's age in the hypothesis contradicts her age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
