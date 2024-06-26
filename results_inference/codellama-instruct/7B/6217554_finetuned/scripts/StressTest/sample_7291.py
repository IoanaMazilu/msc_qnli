cookies_premise = 500
cookies_hypothesis = 600

# the hypothesis talks about the number of cookies, referenced also in the premise
if cookies_hypothesis <= cookies_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cookies_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cookies
    # any number of cookies greater than 'cookies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
