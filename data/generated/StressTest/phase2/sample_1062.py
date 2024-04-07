# Premise: It could go 4 times as fast as Mohan’s old Mercedes.
# Hypothesis: It could go more than 1 times as fast as Mohan’s old Mercedes.
# Golden Label: entailment

speed_multiple_premise = 4
speed_multiple_hypothesis = 1

# the hypothesis refers to the speed multiple of Mohan's old Mercedes mentioned in the premise
if speed_multiple_premise <= speed_multiple_hypothesis:
    # check if the 'speed_multiple_hypothesis' contradicts the speed multiple in the premise
    label = "contradiction"
elif speed_multiple_hypothesis > speed_multiple_premise:
    # check if the 'speed_multiple_hypothesis' contradicts the speed multiple reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

