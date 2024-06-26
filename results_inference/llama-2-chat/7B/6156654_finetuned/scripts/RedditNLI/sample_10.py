rupee_value_premise = 65.36
rupee_value_hypothesis = 68.19
sensex_fall_premise = 300
sensex_fall_hypothesis = 282.50
nifty_future_trading_call_premise = "Tuesday 27 Aug"
nifty_future_trading_call_hypothesis = "Wednesday 28 Aug"

# the hypothesis refers to the same events and time periods as the premise
if rupee_value_hypothesis!= rupee_value_premise:
    # check if the value of rupee in the hypothesis contradicts the value of rupee in the premise
    label = "contradiction"
elif sensex_fall_hypothesis!= sensex_fall_premise:
    # check if the fall of sensex in the hypothesis contradicts the fall of sensex in the premise
    label = "contradiction"
elif nifty_future_trading_call_hypothesis!= nifty_future_trading_call_premise:
    # check if the nifty future trading call day in the hypothesis contradicts the nifty future trading call day in the premise
    label = "contradiction"
else:
    # if the hypothesis values and dates match the premise values and dates, we can infer entailment
    label = "entailment"

print(label)
