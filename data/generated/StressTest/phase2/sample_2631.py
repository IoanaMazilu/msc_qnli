# Premise: While driving from City A to City B, Bob drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Bob drives at a constant speed of more than 30 miles per hour.
# Golden Label: entailment

speed_premise = 40
speed_hypothesis = 30

# the hypothesis talks about the speed of Bob's driving from City A to City B, as mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis that Bob drives at a speed more than 'speed_hypothesis'
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
