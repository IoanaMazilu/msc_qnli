# Premise: At the end of'n'years, Sandy got back 7 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back more than 4 times the original investment.
# Golden Label: entailment

times_investment_premise = 7
times_investment_hypothesis = 4

# the hypothesis refers to the multiple of the original investment that Sandy got back, which is also mentioned in the premise
if times_investment_premise < times_investment_hypothesis:
    # check if the number of times of investment in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif times_investment_premise > times_investment_hypothesis:
    # if the number of times of investment in the premise is greater than in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of times of investment in the premise is equal to the number in the hypothesis, it is neutral as it doesn't fully entail nor contradict
    label = "neutral"

print(label)

