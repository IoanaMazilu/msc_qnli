# Premise: Murali travelled from city A to city B at a speed of less than 80 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Golden Label: neutral

speed_AB_premise = 80
speed_BC_premise = 60

speed_AB_hypothesis = 40
speed_BC_hypothesis = 60

# the hypothesis talks about the speeds of travel from A to B and B to C, which are also referenced in the premise
if speed_AB_hypothesis >= speed_AB_premise:
    # check if the speed from A to B in the hypothesis contradicts the premise's estimate of less than 'speed_AB_premise'
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from B to C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

