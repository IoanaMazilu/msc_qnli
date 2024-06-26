anand_investment_premise = 82500
deepak_investment_premise = 35000
anand_investment_hypothesis = 22500
deepak_investment_hypothesis = 35000

# the hypothesis refers to the investments made by Anand and Deepak, also mentioned in the premise
if anand_investment_hypothesis >= anand_investment_premise:
    # check if the estimated investment of Anand in the hypothesis contradicts the premise
    label = "contradiction"
elif deepak_investment_hypothesis != deepak_investment_premise:
    # check if Deepak's investment in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis investments do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
