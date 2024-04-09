opec_cuts_premise = 68
opec_cuts_hypothesis = 28
price_rally_premise = 5

# the hypothesis refers to the percentage of price slump in the last 3 months and the expected price rally
if opec_cuts_hypothesis <= opec_cuts_premise:
    # check if the estimate of 'opec_cuts_hypothesis' contradicts the percentage of price slump in the premise
    label = "contradiction"
elif price_rally_premise!= price_rally_hypothesis:
    # check if the expected price rally in the hypothesis contradicts the expected price rally in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
