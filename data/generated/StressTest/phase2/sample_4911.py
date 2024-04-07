# Premise: Tom drives from town E to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town E to town B, driving at a constant speed of more than 30 miles per hour.
# Golden Label: entailment

speed_premise = 60
speed_hypothesis = 30

# the hypothesis talks about the speed at which Tom drives, which is also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the driving speed in the premise contradicts the estimate of 'speed_hypothesis'
    label = "contradiction"
else:
    # if the driving speed in the premise does not contradict the 'speed_hypothesis', we can infer entailment
    label = "entailment"

print(label)

