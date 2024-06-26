kiwi_fruit_premise = 5
kiwi_fruit_hypothesis = 8

# the hypothesis talks about the quantity of kiwi fruit bought by Smitha, referenced also in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kiwi_fruit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of kiwi fruit
    # any quantity greater than 'kiwi_fruit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
