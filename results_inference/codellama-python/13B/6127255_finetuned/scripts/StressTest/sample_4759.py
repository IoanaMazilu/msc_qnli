outfit_shirt_premise = 5
outfit_shirt_hypothesis = 1

# the hypothesis talks about the number of shirts in an outfit, referenced also in the premise
if outfit_shirt_hypothesis >= outfit_shirt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'outfit_shirt_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than 'outfit_shirt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
