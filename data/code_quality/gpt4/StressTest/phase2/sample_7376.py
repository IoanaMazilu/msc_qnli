shifts_premise = 16
shifts_hypothesis = 16
orders_per_hour = 40

# the hypothesis talks about the number of shifts worked in a week, referenced also in the premise
if shifts_hypothesis != shifts_premise:
    # check if the hypothesis value contradicts the number of shifts mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
