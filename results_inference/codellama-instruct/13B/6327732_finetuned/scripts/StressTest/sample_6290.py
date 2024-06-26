kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 8

# the hypothesis refers to the number of kiwi fruit bought and the average rate mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the estimate of 'kiwi_fruit_hypothesis' contradicts the number of kiwi fruit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kiwi fruit
    # any number of kiwi fruit greater than 'kiwi_fruit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
