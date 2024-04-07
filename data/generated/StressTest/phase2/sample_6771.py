# Premise: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of less than 50 kmph and from city B to city C at 60 kmph.
# Golden Label: entailment

speed_AB_premise = 40
speed_BC_premise = 60
speed_AB_hypothesis = 50
speed_BC_hypothesis = 60

# the hypothesis refers to the speeds of Murali's travels mentioned in the premise
if speed_AB_premise >= speed_AB_hypothesis:
    # check if the estimate of 'speed_AB_hypothesis' contradicts the speed from city A to city B in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from city B to city C in the hypothesis contradicts the respective speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

