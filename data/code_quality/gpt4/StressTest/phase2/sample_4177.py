burj_khalifa_height_premise = 730
burj_khalifa_height_hypothesis = 830
sears_height_premise = 527
sears_height_hypothesis = 527

# the hypothesis talks about the height of Burj Khalifa and Sears, referenced also in the premise
if burj_khalifa_height_hypothesis <= burj_khalifa_height_premise:
    # check if the hypothesis value contradicts the estimate of more than 'burj_khalifa_height_premise'
    label = "contradiction"
elif sears_height_hypothesis != sears_height_premise:
    # check if the height of Sears in the hypothesis contradicts the height of Sears reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of Burj Khalifa
    # any height of Burj Khalifa greater than 'burj_khalifa_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
