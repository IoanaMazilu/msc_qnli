bananas_added = 5.0
original_bananas = 46.0
bananas_left = 51.0

# the hypothesis refers to the number of bananas left in the jar, which is also mentioned in the premise
if bananas_left!= (original_bananas + bananas_added):
    # check if the number of bananas left in the jar contradicts the number of bananas added and the original number of bananas
    label = "contradiction"
else:
    # if the hypothesis values and calculations do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
