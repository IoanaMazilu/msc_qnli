current_age_premise = 18
current_age_hypothesis = 18
past_age_premise = 7
past_age_hypothesis = 7

# the hypothesis refers to Molly's age in the future and in the past, mentioned in the premise
if current_age_hypothesis <= current_age_premise:
    # check if the estimate of 'current_age_hypothesis' contradicts the current age in the premise
    label = "contradiction"
elif past_age_hypothesis!= past_age_premise:
    # check if the past age in the hypothesis contradicts the past age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
