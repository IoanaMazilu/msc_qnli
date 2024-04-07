# Premise: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of more than 10 kmph and from city B to city C at 60 kmph.
# Golden Label: entailment

speed_AB_premise = 40
speed_AB_hypothesis = 10
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speeds of Murali's travel mentioned in the premise
if speed_AB_premise <= speed_AB_hypothesis:
    # check if the estimate of 'speed_AB_hypothesis' contradicts the speed of travel from city A to B in the premise
    label = "contradiction"
elif speed_BC_premise != speed_BC_hypothesis:
    # check if the speed of travel from city B to C in the hypothesis contradicts the speed of travel from city B to C in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

