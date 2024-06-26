sacha_speed_premise = 1
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speed of Sacha and Bruno mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the speed of'sacha_speed_hypothesis' contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Sacha
    # any speed of Sacha greater than'sacha_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
