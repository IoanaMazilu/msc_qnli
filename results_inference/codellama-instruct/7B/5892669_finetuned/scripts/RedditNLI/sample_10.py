rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_premise = 27
nifty_hypothesis = 28

# the hypothesis and premise mention the value of Rupee, Sensex and Nifty
if rupee_premise!= rupee_hypothesis:
    # check if the value of Rupee in the hypothesis contradicts the value of Rupee in the premise
    label = "contradiction"
elif sensex_premise!= sensex_hypothesis:
    # check if the value of Sensex in the hypothesis contradicts the value of Sensex in the premise
    label = "contradiction"
elif nifty_premise!= nifty_hypothesis:
    # check if the value of Nifty in the hypothesis contradicts the value of Nifty in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
