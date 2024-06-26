walking_rate_matthew_premise = 5
walking_rate_johnny_premise = 4
walking_rate_matthew_hypothesis = 3
walking_rate_johnny_hypothesis = 4

# the hypothesis talks about the walking rate of Matthew and Johnny
if walking_rate_matthew_hypothesis <= walking_rate_matthew_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walking_rate_matthew_premise'
    label = "contradiction"
elif walking_rate_johnny_hypothesis <= walking_rate_johnny_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walking_rate_johnny_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
