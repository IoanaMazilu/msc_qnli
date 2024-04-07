# Premise: Tom drives from town W to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town W to town B, driving at a constant speed of more than 40 miles per hour.
# Golden Label: entailment

speed_premise = 60
speed_hypothesis = 40

# the hypothesis refers to the speed of driving from town W to town B mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the 'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
