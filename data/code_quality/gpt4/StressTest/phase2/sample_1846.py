investment_return_premise = 8
investment_return_hypothesis = 3

# the hypothesis talks about the return on investment at the end of 'n' years, referenced also in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_return_premise'
    label = "contradiction"
elif investment_return_hypothesis < investment_return_premise:
    # any return on investment less than 'investment_return_premise' is consistent with the premise
    # since the return is explicitly 3 times in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
