floors_premise = 51
floors_hypothesis = 81
rate_per_minute_premise = 63

# the hypothesis talks about the floor where Albert gets on the elevator and the rate at which he rides down
if floors_hypothesis <= floors_premise:
    # check if the hypothesis value contradicts the estimate of 'floors_premise'
    label = "contradiction"
elif floors_premise!= rate_per_minute_premise:
    # check if the number of floors per minute in the hypothesis contradicts the number of floors per minute reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
