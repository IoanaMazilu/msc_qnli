# Premise: Shridhar is less than 6:2.
# Hypothesis: Shridhar is 3:2.
# Golden Label: neutral

shridhar_height_premise = 6.2
shridhar_height_hypothesis = 3.2

# the hypothesis makes a statement about Shridhar's height which is also mentioned in the premise
if shridhar_height_hypothesis >= shridhar_height_premise:
    # check if the height in the hypothesis contradicts the estimate of less than 'shridhar_height_premise'
    label = "contradiction"
elif shridhar_height_hypothesis == shridhar_height_premise:
    # check if the height in the hypothesis equals the 'shridhar_height_premise', which would contradict the 'less than' statement in the premise
    label = "contradiction"
else:
    # the premise gives an estimate that Shridhar's height is less than 6.2
    # a height of 3.2 is consistent with the premise, so it can be explicitly entailed from the premise
    label = "entailment"

print(label)

