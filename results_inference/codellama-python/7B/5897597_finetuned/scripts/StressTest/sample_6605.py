investment_return_premise = 2
investment_return_hypothesis = 2

# the hypothesis refers to the return on investment after 'n' years, which is also mentioned in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the hypothesis value contradicts the premise value of 'investment_return_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
