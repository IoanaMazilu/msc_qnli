premise_age_ratio = 3/4
hypothesis_age_ratio = 3/4
premise_age_difference = 5
hypothesis_age_difference = 2

# check if the hypothesis age difference contradicts the premise age difference
if hypothesis_age_difference!= premise_age_difference:
    label = "contradiction"
# check if the hypothesis age ratio contradicts the premise age ratio
elif hypothesis_age_ratio!= premise_age_ratio:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
