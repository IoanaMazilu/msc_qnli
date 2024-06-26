mary_investment_premise = 700
harry_investment_premise = 300
mary_investment_hypothesis = 200
harry_investment_hypothesis = 300

# the hypothesis talks about the investments made by Mary and Harry, referenced also in the premise
if mary_investment_hypothesis != mary_investment_premise:
    # check if Mary's investment in the hypothesis contradicts Mary's investment in the premise
    label = "contradiction"
elif harry_investment_hypothesis != harry_investment_premise:
    # check if Harry's investment in the hypothesis contradicts Harry's investment in the premise
    label = "contradiction"
else:
    # if the investments in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
