years_premise = 6
years_hypothesis = 2
age_premise = 30
age_hypothesis = 30

# the hypothesis refers to the age of Sandy after a certain number of years, mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
