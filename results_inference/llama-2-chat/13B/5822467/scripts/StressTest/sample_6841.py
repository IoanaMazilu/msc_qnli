premise_investment = 20000
premise_time = 7
hypothesis_time = 6

# define variables for the numerical entities in the premise and hypothesis
investment_premise = premise_investment / premise_time
investment_hypothesis = hypothesis_time * premise_investment / 12

# compare the variables to determine the label
if investment_premise <= investment_hypothesis:
    label = "entailment"
elif investment_hypothesis > investment_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
