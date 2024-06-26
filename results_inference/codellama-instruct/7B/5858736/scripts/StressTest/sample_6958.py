toy_purchases_premise = 20
toy_purchases_hypothesis = 20
toy_rate_premise = 275
toy_rate_hypothesis = 375

# the hypothesis refers to the number of toy purchases and the rate at which they were made
if toy_purchases_premise <= toy_purchases_hypothesis:
    # check if the estimate of 'toy_purchases_hypothesis' contradicts the number of toy purchases in the premise
    label = "contradiction"
elif toy_rate_hypothesis <= toy_rate_premise:
    # check if the rate at which the toys were purchased in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
