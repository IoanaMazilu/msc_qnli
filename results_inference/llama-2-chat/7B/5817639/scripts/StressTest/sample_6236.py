speed_premise = 2
speed_hypothesis = 1

# the hypothesis talks about Anne's speed being doubled, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
