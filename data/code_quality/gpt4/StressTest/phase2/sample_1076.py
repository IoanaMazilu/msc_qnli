tom_profit_more_than_jerry_premise = 800
tom_profit_more_than_jerry_hypothesis = 200

# the hypothesis talks about the profit difference between Tom and Jerry, stated also in the premise
if tom_profit_more_than_jerry_hypothesis != tom_profit_more_than_jerry_premise:
    # check if the profit difference in the hypothesis contradicts the profit difference stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)
