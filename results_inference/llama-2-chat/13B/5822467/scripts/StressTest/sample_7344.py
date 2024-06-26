opec_cuts_premise = 28
opec_cuts_hypothesis = 68
price_rally_premise = 5

# the hypothesis refers to the price slump and the expected rally
if opec_cuts_hypothesis < opec_cuts_premise:
    # check if the estimate of 'opec_cuts_hypothesis' contradicts the price slump reported in the premise
    label = "contradiction"
elif price_rally_premise!= price_rally_hypothesis:
    # check if the expected rally in the hypothesis contradicts the expected rally reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
