# Premise: Henry runs the second leg of the course in more than 6 seconds.
# Hypothesis: Henry runs the second leg of the course in 7 seconds.
# Golden Label: neutral

second_leg_premise = 6
second_leg_hypothesis = 7

# the hypothesis specifies the time Henry takes to run the second leg of the course, which is also referred to in the premise
if second_leg_hypothesis <= second_leg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'second_leg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the run time
    # any run time greater than 'second_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

