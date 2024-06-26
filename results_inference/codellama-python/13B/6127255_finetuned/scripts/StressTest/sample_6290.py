kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 8
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the amount of kiwi fruit bought by Smitha and the average rate, mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kiwi_fruit_premise'
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of kiwi fruit
    # any amount of kiwi fruit greater than 'kiwi_fruit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
