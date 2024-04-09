investment_return_premise = 3
investment_return_hypothesis = 2

# the hypothesis refers to the return on investment after 'n' years, which is also mentioned in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_return_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the return on investment
    # any return on investment less than 'investment_return_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
