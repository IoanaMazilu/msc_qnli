 savings_premise = 21
allowance_premise = 15
wins_premise = 6
money_now_hypothesis = 220.0

# the hypothesis mentions the current amount of money, which is also referenced in the premise
# compute the current amount of money in the premise
money_now_premise = savings_premise + allowance_premise + wins_premise
if money_now_hypothesis!= money_now_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money from the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are equal, we can infer entailment
    label = "entailment"

print(label)
