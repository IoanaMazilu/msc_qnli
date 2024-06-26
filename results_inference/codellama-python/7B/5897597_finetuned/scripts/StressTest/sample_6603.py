investment_return_premise = 2
investment_return_hypothesis = 3

# the hypothesis refers to the return on investment after 'n' years, mentioned in the premise
if investment_return_hypothesis <= investment_return_premise:
    # check if the hypothesis value contradicts the return on investment in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
