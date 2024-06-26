leo_gain_premise = 50
leo_gain_hypothesis = 10

# the hypothesis talks about the weight gain of Leo, referenced also in the premise
if leo_gain_hypothesis >= leo_gain_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leo_gain_premise'
    label = "contradiction"
elif leo_gain_hypothesis < leo_gain_premise:
    # the premise gives only an estimate for the weight gain of Leo
    # any weight gain less than 'leo_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
