future_age_premise = 18
past_age_premise = 7
future_age_hypothesis = 18
past_age_hypothesis = 7

# the hypothesis refers to the future and past ages of Molly mentioned in the premise
if future_age_hypothesis <= future_age_premise:
    # check if the estimate of 'future_age_hypothesis' contradicts the number of future years in the premise
    label = "contradiction"
elif past_age_hypothesis!= past_age_premise:
    # check if the number of past years in the hypothesis contradicts the number of past years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
