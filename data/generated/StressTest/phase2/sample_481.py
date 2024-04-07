# Premise: On her way back, Swetha drives less than 80 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Hypothesis: On her way back, Swetha drives 30 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Golden Label: neutral

speed_premise = 80
speed_hypothesis = 30

# the hypothesis refers to the speed Swetha drives on her way back, also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the speed less than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

