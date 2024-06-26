steps_premise = 60
steps_hypothesis = 80

# the hypothesis talks about the number of steps Vinod climbs, referenced also in the premise
if steps_premise >= steps_hypothesis:
    # check if the number of steps in the premise contradicts the estimate of less than'steps_hypothesis'
    label = "contradiction"
else:
    # if the premise values do not contradict the hypothesis ones, we can infer entailment
    label = "entailment"

print(label)