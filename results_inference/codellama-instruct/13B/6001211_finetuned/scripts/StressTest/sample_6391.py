sacha_speed_premise = 1
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the running speed of Bruno in the hypothesis contradicts the running speed of Bruno reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the running speed of Sacha
    # any speed greater than'sacha_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)