yhat_premise = 28
yhat_hypothesis = 38

# the hypothesis talks about the time Dawson took to run the first leg of the course, referenced also in the premise
if yhat_hypothesis <= yhat_premise:
    # check if the hypothesis value contradicts the estimate of more than 'yhat_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'yhat_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

