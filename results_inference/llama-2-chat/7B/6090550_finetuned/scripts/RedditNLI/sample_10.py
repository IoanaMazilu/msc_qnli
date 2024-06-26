rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_future_call_premise = 'Tuesday 27 Aug'
nifty_future_call_hypothesis = 'Wednesday 28 Aug'

# the hypothesis talks about the rupee value, sensex fall, and nifty future trading call on a specific date
if rupee_hypothesis!= rupee_premise:
    # check if the rupee value in the hypothesis contradicts the rupee value in the premise
    label = "contradiction"
elif sensex_hypothesis!= sensex_premise:
    # check if the sensex fall in the hypothesis contradicts the sensex fall in the premise
    label = "contradiction"
elif nifty_future_call_hypothesis!= nifty_future_call_premise:
    # check if the nifty future trading call date in the hypothesis contradicts the nifty future trading call date in the premise
    label = "contradiction"
else:
    # if the hypothesis values and dates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
