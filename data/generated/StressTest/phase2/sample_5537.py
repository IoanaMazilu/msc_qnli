# Premise: Anand and Deepak started a business investing Rs 22500 and 35000 respectively.
# Hypothesis: Anand and Deepak started a business investing Rs more than 22500 and 35000 respectively.
# Golden Label: contradiction

anand_investment_premise = 22500
anand_investment_hypothesis = 22500
deepak_investment_premise = 35000
deepak_investment_hypothesis = 35000

# the hypothesis refers to the investment of Anand and Deepak mentioned in the premise
if anand_investment_hypothesis <= anand_investment_premise:
    # check if the hypothesis value contradicts the investment of Anand in the premise
    label = "contradiction"
elif deepak_investment_hypothesis != deepak_investment_premise:
    # check if the investment of Deepak in the hypothesis contradicts the investment of Deepak in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

