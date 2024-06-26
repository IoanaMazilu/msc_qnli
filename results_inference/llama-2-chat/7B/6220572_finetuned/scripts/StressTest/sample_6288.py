kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 5
rate_kiwi_fruit_premise = 360
rate_kiwi_fruit_hypothesis = 360

# the hypothesis refers to the number of kg and average rate of kiwi fruit mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the estimate of 'kiwi_fruit_hypothesis' contradicts the number of kg of kiwi fruit in the premise
    label = "contradiction"
elif rate_kiwi_fruit_hypothesis!= rate_kiwi_fruit_premise:
    # check if the average rate of kiwi fruit in the hypothesis contradicts the average rate of kiwi fruit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
