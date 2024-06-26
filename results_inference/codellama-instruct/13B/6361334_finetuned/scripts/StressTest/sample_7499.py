current_age_premise = 34
current_age_hypothesis = 44
years_since_stopped_baby_sitting_premise = 10
years_since_stopped_baby_sitting_hypothesis = 10

# the hypothesis refers to the current age and the number of years since stopped baby-sitting mentioned in the premise
if current_age_hypothesis!= current_age_premise:
    # check if the current age in the hypothesis contradicts the current age in the premise
    label = "contradiction"
elif years_since_stopped_baby_sitting_hypothesis!= years_since_stopped_baby_sitting_premise:
    # check if the number of years since stopped baby-sitting in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
