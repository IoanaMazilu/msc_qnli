original_investment_premise = float(input("Original investment: "))
original_investment_hypothesis = float(input("Hypothesis: "))

# the hypothesis talks about the amount of return on investment, referenced also in the premise
if original_investment_hypothesis <= original_investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'original_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of return on investment
    # any amount of return on investment greater than 'original_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
