kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 8

# the hypothesis refers to the number of kiwi fruit bought, mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the estimate of 'kiwi_fruit_hypothesis' contradicts the number of kiwi fruit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
