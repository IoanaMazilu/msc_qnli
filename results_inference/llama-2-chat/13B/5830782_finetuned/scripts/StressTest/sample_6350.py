investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the investment made by Mr Praveen, which is also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact amount for the investment
    # any investment greater than 'investment_premise' contradicts the premise
    label = "contradiction"

print(label)
