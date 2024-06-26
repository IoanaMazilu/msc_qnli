sacha_speed_premise = 9
sacha_speed_hypothesis = 9
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis talks about the speed of Sacha and Bruno, referenced also in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Sacha and Bruno
    # any speed greater than'sacha_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
