john_investment_premise = 700
john_investment_hypothesis = 600
mike_investment_premise = 300
mike_investment_hypothesis = 300

# the hypothesis talks about the investments made by John and Mike which are also referenced in the premise
if john_investment_premise <= john_investment_hypothesis:
    # check if the hypothesis value contradicts the exact investment made by John as per the premise
    label = "contradiction"
elif mike_investment_hypothesis != mike_investment_premise:
    # check if the hypothesis value contradicts the exact investment made by Mike as per the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
