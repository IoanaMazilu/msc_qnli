kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 9
rate_premise = 360
rate_hypothesis = 360

# the hypothesis talks about the number of kiwi fruit bought and the rate at which they were bought, both of which are also mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the hypothesis value contradicts the estimate of 'kiwi_fruit_premise'
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate at which kiwi fruit were bought in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
