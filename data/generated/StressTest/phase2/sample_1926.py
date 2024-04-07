# Premise: Cara drives at a constant speed of 32 km per hour.
# Hypothesis: Cara drives at a constant speed of more than 12 km per hour.
# Golden Label: entailment

speed_premise = 32
speed_hypothesis = 12

# the hypothesis talks about the speed at which Cara drives, which is also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of more than 'speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

