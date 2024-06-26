mary_profit_premise = 800
mary_profit_hypothesis = 500

# the hypothesis refers to the profit Mary made, which is also mentioned in the premise
if mary_profit_premise < mary_profit_hypothesis:
    # check if the profit made by Mary in the hypothesis contradicts the profit reported in the premise
    label = "contradiction"
elif mary_profit_premise > mary_profit_hypothesis:
    # check if the profit made by Mary in the hypothesis can be entailed from the premise
    label = "entailment"
else:
    # if the profit made by Mary in the hypothesis does not contradict or can be entailed from the premise, we infer neutrality
    label = "neutral"

print(label)
