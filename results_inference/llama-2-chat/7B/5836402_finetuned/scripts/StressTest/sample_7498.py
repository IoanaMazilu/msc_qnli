jane_age_premise = 54
jane_age_hypothesis = 34
baby_sitting_years_premise = 10
baby_sitting_years_hypothesis = 10

# the hypothesis talks about Jane's age and the number of years she stopped baby-sitting, which are also mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jane_age_premise'
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years Jane stopped baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
