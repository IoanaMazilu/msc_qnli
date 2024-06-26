jane_age_premise = 32
jane_age_hypothesis = 32
baby_sitting_years_premise = 10
baby_sitting_years_hypothesis = 10

# the hypothesis refers to the age of Jane and the years she stopped baby-sitting, as mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the age of Jane in the premise
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years Jane stopped baby-sitting in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
