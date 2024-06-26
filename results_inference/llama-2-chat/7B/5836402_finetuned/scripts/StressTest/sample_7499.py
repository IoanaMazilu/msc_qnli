jane_age_premise = 34
jane_age_hypothesis = 44
stop_baby_sitting_years_premise = 10
stop_baby_sitting_years_hypothesis = 10

# the hypothesis refers to the current age of Jane and the years she stopped baby-sitting, as mentioned in the premise
if jane_age_hypothesis!= jane_age_premise:
    # check if the current age in the hypothesis contradicts the current age reported in the premise
    label = "contradiction"
elif stop_baby_sitting_years_hypothesis!= stop_baby_sitting_years_premise:
    # check if the number of years Jane stopped baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
