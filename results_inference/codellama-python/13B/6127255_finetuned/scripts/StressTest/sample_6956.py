average_shirts_premise = 40
average_shirts_hypothesis = 40
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise + shirts_purchased:
    # check if the hypothesis value contradicts the premise value after the purchase
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise + shirts_purchased:
    # check if the hypothesis value is less than the premise value after the purchase
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
