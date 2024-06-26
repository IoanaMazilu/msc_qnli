jane_age_premise = 54
jane_age_hypothesis = 34
baby_sitting_years_premise = 12
baby_sitting_years_hypothesis = 12

# the hypothesis refers to Jane's age and the number of years ago she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the 'jane_age_hypothesis' contradicts the estimate of less than 'jane_age_premise'
    label = "contradiction"
elif baby_sitting_years_hypothesis != baby_sitting_years_premise:
    # check if the number of years Jane stopped baby-sitting in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif jane_age_hypothesis <= jane_age_premise and baby_sitting_years_hypothesis == baby_sitting_years_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
