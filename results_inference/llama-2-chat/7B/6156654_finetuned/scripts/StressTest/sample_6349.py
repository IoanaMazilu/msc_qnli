investment_premise = 30000
investment_hypothesis = 90000

# the hypothesis talks about the investment made by Mr Praveen, which is also mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the investment amounts are the same, we can infer entailment
    label = "entailment"

print(label)
