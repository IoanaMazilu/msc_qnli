# Premise: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of less than 80 kmph and from city B to city C at 60 kmph.
# Golden Label: entailment

speed_AB_premise = 40
speed_BC_premise = 60
speed_AB_hypothesis = 80
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel between cities as stated in the premise
if speed_AB_premise > speed_AB_hypothesis:
    # check if the speed of travel from A to B in the premise contradicts the hypothesis estimate of less than 'speed_AB_hypothesis'
    label = "contradiction"
elif speed_BC_premise != speed_BC_hypothesis:
    # check if the speed of travel from B to C in the premise contradicts the one in the hypothesis
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)

