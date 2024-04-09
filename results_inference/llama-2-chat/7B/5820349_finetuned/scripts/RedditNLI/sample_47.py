drained_value_turkey_premise = 5.12
drained_value_poland_hypothesis = 1

# the hypothesis and premise mention the amount drained out of the economy due to current account deficit
# but the countries and months mentioned are different
if drained_value_turkey_premise!= drained_value_poland_hypothesis:
    # check if the drained amount in the hypothesis contradicts the drained amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
