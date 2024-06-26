ashok_investment_premise = 1/9
ashok_investment_hypothesis = 5/9

# the hypothesis talks about the share of Ashok and Pyarelal's investment, referenced also in the premise
if ashok_investment_hypothesis != ashok_investment_premise:
    # check if the hypothesis value contradicts the estimate of 'ashok_investment_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
