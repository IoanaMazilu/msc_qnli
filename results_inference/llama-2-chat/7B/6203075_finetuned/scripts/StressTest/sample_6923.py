earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the same situation as the premise, but with a different earnings value
if earnings_hypothesis!= earnings_premise:
    # check if the earnings value in the hypothesis contradicts the earnings value in the premise
    label = "contradiction"
else:
    # if the earnings value in the hypothesis does not contradict the earnings value in the premise, we can infer entailment
    label = "entailment"

print(label)
