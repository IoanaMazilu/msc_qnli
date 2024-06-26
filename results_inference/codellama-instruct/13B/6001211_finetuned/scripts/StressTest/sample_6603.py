investment_return_premise = 2
investment_return_hypothesis = 3

# the hypothesis refers to the return on investment after 'n' years, mentioned in the premise
if investment_return_premise >= investment_return_hypothesis:
    # check if the 'investment_return_premise' contradicts the hypothesis that she got back less than 3 times the investment
    label = "contradiction"
else:
    # if the 'investment_return_premise' does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
