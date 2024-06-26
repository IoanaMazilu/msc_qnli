risk_increase_premise = 0.44
risk_increase_hypothesis = 0.44

# The hypothesis mentions the increased risk of a teen driver crashing when passengers are present, which is also mentioned in the premise
# However, the hypothesis does not specify that the crash could be fatal, which is mentioned in the premise

if risk_increase_hypothesis != risk_increase_premise:
    # Check if the increase in risk according to the hypothesis contradicts the increase in risk reported in the premise
    label = "contradiction"
else:
    # If the increase in risk in the hypothesis does not contradict the increase in risk in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
