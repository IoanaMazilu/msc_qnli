investment_premise = 25000
investment_hypothesis = 75000

# the hypothesis talks about the investment made by Mr Shivkumar in the business, which is also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the 'investment_premise'
    label = "contradiction"
elif investment_premise != investment_hypothesis:
    # check if the investment amount in the hypothesis contradicts the investment made in the premise
    label = "entailment"
else:
    # the premise gives the exact amount for the investment
    # any investment amount less than 'investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
