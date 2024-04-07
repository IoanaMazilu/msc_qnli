# Premise: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of more than 20 kmph and from city B to city C at 60 kmph.
# Golden Label: entailment

speed_A_to_B_premise = 40
speed_A_to_B_hypothesis = 20
speed_B_to_C_premise = 60
speed_B_to_C_hypothesis = 60

# the hypothesis refers to the speeds of travel between the same cities mentioned in the premise
if speed_A_to_B_premise <= speed_A_to_B_hypothesis:
    # check if the estimate of 'speed_A_to_B_hypothesis' contradicts the speed of travel from city A to B in the premise
    label = "contradiction"
elif speed_B_to_C_premise != speed_B_to_C_hypothesis:
    # check if the speed of travel from city B to C in the hypothesis contradicts the speed of travel from city B to C reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

