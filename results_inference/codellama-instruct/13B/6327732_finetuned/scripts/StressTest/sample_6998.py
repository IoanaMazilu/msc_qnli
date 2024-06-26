sacha_speed_premise = 9
sacha_speed_hypothesis = 9
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha, which is also mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the estimate of'sacha_speed_hypothesis' contradicts the speed of Sacha in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Sacha
    # any speed greater than'sacha_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
