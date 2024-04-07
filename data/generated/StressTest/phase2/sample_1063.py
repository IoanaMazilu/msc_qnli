# Premise: It could go more than 1 times as fast as Mohan’s old Mercedes.
# Hypothesis: It could go 4 times as fast as Mohan’s old Mercedes.
# Golden Label: neutral

speed_ratio_premise = 1
speed_ratio_hypothesis = 4

# the hypothesis talks about the speed ratio of a vehicle to Mohan's old Mercedes, as stated in the premise
if speed_ratio_hypothesis <= speed_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed ratio
    # any speed ratio greater than 'speed_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

