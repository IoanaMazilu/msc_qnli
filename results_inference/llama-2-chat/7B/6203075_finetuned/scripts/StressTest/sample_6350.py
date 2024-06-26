investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the investment made by Mr Praveen, mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
