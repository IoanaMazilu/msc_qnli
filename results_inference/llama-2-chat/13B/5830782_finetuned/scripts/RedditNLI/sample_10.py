rupee_value_premise = 65.36
rupee_value_hypothesis = 68.19
sensex_fall_premise = 300
sensex_fall_hypothesis = 282.50

# the hypothesis and premise mention the rupee value, sensex fall, and nifty future trading call
if rupee_value_premise!= rupee_value_hypothesis:
    # check if the rupee value in the hypothesis contradicts the rupee value in the premise
    label = "contradiction"
elif sensex_fall_premise!= sensex_fall_hypothesis:
    # check if the sensex fall in the hypothesis contradicts the sensex fall in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
