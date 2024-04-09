rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_future_trading_call_day_premise = 27
nifty_future_trading_call_day_hypothesis = 28

# the hypothesis and premise mention the value of the rupee, the sensex and the nifty future trading call day
if rupee_premise!= rupee_hypothesis:
    # check if the rupee value in the hypothesis contradicts the rupee value in the premise
    label = "contradiction"
elif sensex_premise!= sensex_hypothesis:
    # check if the sensex value in the hypothesis contradicts the sensex value in the premise
    label = "contradiction"
elif nifty_future_trading_call_day_premise!= nifty_future_trading_call_day_hypothesis:
    # check if the nifty future trading call day in the hypothesis contradicts the nifty future trading call day in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
