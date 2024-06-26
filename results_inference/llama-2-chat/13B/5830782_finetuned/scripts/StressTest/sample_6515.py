john_age_factor_premise = 3
john_age_factor_hypothesis = 3
years_back_premise = 6
years_back_hypothesis = 2

# the hypothesis talks about the age relation between John and Tom at a certain point in the past, which is also mentioned in the premise
if john_age_factor_premise!= john_age_factor_hypothesis:
    # check if the age factor in the hypothesis contradicts the age factor in the premise
    label = "contradiction"
elif years_back_hypothesis!= years_back_premise:
    # check if the number of years back in the hypothesis contradicts the number of years back in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
