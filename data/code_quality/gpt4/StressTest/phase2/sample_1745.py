investment_return_premise = 4
investment_return_hypothesis = 2

# the hypothesis talks about the return on investment after 'n' years, which is also referenced in the premise
if investment_return_hypothesis != investment_return_premise:
    # check if the return on investment in the hypothesis contradicts the return on investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
