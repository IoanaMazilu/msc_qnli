premise_age = 30
hypothesis_age = 30
years_premise = 6
years_hypothesis = "more than 2"

# the hypothesis talks about the age of Sandy after a certain number of years
if hypothesis_age <= premise_age:
    # check if the hypothesis value contradicts the estimate of 'premise_age'
    label = "contradiction"
elif years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
