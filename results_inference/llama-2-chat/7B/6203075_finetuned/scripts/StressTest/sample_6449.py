john_age_in_years_premise = 5
john_age_in_years_hypothesis = 7

# the hypothesis talks about John's age in the future, which is also referenced in the premise
if john_age_in_years_hypothesis!= john_age_in_years_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
