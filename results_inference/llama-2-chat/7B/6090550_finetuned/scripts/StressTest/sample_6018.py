 age_premise = 32
age_hypothesis = 42
baby_sitting_years_premise = 10
baby_sitting_years_hypothesis = 10

# the hypothesis talks about Jane's current age and the number of years she stopped baby-sitting, both referenced in the premise
if age_hypothesis < age_premise:
    # check if the hypothesis value contradicts the age in the premise
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years she stopped baby-sitting in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
