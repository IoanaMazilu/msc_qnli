age_premise = 34
age_hypothesis = 44
years_baby_sitting_premise = 10
years_baby_sitting_hypothesis = 10

# the hypothesis refers to the age and the number of years baby-sitting mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the hypothesis value contradicts the age in the premise
    label = "contradiction"
elif years_baby_sitting_hypothesis!= years_baby_sitting_premise:
    # check if the number of years baby-sitting in the hypothesis contradicts the number of years baby-sitting reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
