age_premise = 40
age_hypothesis = 40
years_premise = 5
years_hypothesis = 2

# the hypothesis refers to the age of Arun after a certain number of years, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
elif years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)