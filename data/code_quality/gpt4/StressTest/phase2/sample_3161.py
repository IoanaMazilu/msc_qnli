investment_return_premise = 5
investment_return_hypothesis = 6

# the hypothesis refers to the return on investment after 'n' years, which is also mentioned in the premise
if investment_return_hypothesis != investment_return_premise:
    # check if the return on investment in the hypothesis contradicts the return on investment mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
