cookies_michael_premise = 7/8
cookies_michael_hypothesis = 1/8

# the hypothesis refers to the amount of cookies eaten by Michael, mentioned in the premise
if cookies_michael_hypothesis >= cookies_michael_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cookies_michael_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of cookies eaten by Michael
    # any amount of cookies less than 'cookies_michael_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
