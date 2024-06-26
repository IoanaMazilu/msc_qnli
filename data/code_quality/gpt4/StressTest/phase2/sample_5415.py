lary_profit_premise = 800
lary_profit_hypothesis = 200

# the hypothesis refers to the profit Lary made compared to Terry, as stated in the premise
if lary_profit_premise < lary_profit_hypothesis:
    # check if the profit Lary made in the hypothesis contradicts the profit Lary made in the premise
    label = "contradiction"
elif lary_profit_premise > lary_profit_hypothesis:
    # check if the profit Lary made in the hypothesis is less than the profit Lary made in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
