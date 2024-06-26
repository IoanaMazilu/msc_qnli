current_age_premise = 34
current_age_hypothesis = 44
baby_sitting_years_premise = 10
baby_sitting_years_hypothesis = 10

# the hypothesis talks about Jane's current age and the number of years she stopped baby-sitting
if current_age_hypothesis!= current_age_premise:
    # check if the current age in the hypothesis contradicts the current age reported in the premise
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years she stopped baby-sitting in the hypothesis contradicts the number of years she stopped baby-sitting reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
