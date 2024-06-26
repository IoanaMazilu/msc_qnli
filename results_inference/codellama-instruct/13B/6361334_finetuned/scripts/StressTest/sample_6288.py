kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 5
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the number of kg of kiwi fruit bought and the average rate mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the estimate of 'kiwi_fruit_hypothesis' contradicts the number of kg of kiwi fruit in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
