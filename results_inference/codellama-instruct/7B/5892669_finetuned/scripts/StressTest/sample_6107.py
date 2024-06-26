age_jane_premise = 32
age_jane_hypothesis = 32
years_stopped_babysitting_premise = 12
years_stopped_babysitting_hypothesis = 12

# the hypothesis refers to Jane's age and the years she stopped babysitting, mentioned in the premise
if age_jane_hypothesis <= age_jane_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif years_stopped_babysitting_hypothesis!= years_stopped_babysitting_premise:
    # check if the number of years stopped babysitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
