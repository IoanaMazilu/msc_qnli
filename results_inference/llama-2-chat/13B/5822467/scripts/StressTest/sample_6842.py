premise_amount = 20000
premise_duration = 6
hypothesis_duration = "more than 6 months"

# define variables for the premise and hypothesis
rick_investment_premise = premise_amount * premise_duration
rick_investment_hypothesis = hypothesis_duration * premise_amount

# check if the hypothesis contradicts the premise
if rick_investment_hypothesis > rick_investment_premise:
    label = "contradiction"
elif rick_investment_hypothesis == rick_investment_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
