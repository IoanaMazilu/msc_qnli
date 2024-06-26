driving_speed_premise = 70
driving_speed_hypothesis = 60

# the hypothesis talks about James's driving speed and his stopover in Town B, both referenced in the premise
if driving_speed_hypothesis >= driving_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'driving_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
