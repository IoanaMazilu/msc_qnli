butter_premise = 68
butter_hypothesis = 48

# the hypothesis talks about the quantity of butter mixed by Raman, referenced also in the premise
if butter_hypothesis >= butter_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of butter
    # any quantity of butter less than 'butter_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
