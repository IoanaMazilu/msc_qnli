molly_age_premise = 88
molly_age_hypothesis = 18
molly_age_seven_years_ago_premise = 7
molly_age_seven_years_ago_hypothesis = 7

# the hypothesis refers to Molly's age in 18 years, which is also mentioned in the premise
if molly_age_hypothesis!= molly_age_premise:
    # check if the age in 18 years contradicts the age in 88 years
    label = "contradiction"
elif molly_age_seven_years_ago_hypothesis!= molly_age_seven_years_ago_premise:
    # check if the age seven years ago contradicts the age seven years ago
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
