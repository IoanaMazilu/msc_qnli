# Premise: Anand and Deepak started a business investing Rs 22500 and 35000 respectively.
# Hypothesis: Anand and Deepak started a business investing Rs less than 82500 and 35000 respectively.
# Golden Label: entailment

anand_investment_premise = 22500
deepak_investment_premise = 35000
total_investment_hypothesis = 82500
deepak_investment_hypothesis = 35000

# the hypothesis talks about the total investment made by Anand and Deepak in the business, and the individual investment made by Deepak
if (anand_investment_premise + deepak_investment_premise) >= total_investment_hypothesis:
    # check if the total investment value in the hypothesis contradicts the sum of the individual investments made by Anand and Deepak in the premise
    label = "contradiction"
elif deepak_investment_premise != deepak_investment_hypothesis:
    # check if the investment made by Deepak in the hypothesis contradicts the investment made by Deepak in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

