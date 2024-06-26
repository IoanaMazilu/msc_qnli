distance_premise = 80
distance_hypothesis = 20
maxwell_speed = 4
brad_speed = 6

# the hypothesis talks about the distance between their homes and the speeds of Maxwell and Brad, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance between their homes
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
