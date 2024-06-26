speed_premise = 100
speed_hypothesis = 400

# the hypothesis refers to the speed at which Molly and Max are driving, as mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis that they are driving at a rate of less than'speed_hypothesis'
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
