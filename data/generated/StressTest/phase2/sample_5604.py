# Premise: While driving from City A to City B, Glen drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Glen drives at a constant speed of more than 10 miles per hour.
# Golden Label: entailment

driving_speed_premise = 40
driving_speed_hypothesis = 10

# the hypothesis talks about the driving speed of Glen, which is also mentioned in the premise
if driving_speed_premise <= driving_speed_hypothesis:
    # check if the 'driving_speed_premise' contradicts the hypothesis of more than 'driving_speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis speed, we can infer entailment
    label = "entailment"

print(label)

