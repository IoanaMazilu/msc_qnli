purchased_grapes_premise = 1000
purchased_grapes_hypothesis = 700
purchased_mangoes_premise = 900
purchased_mangoes_hypothesis = 900

# the hypothesis talks about the amount of grapes and mangoes purchased
if purchased_grapes_hypothesis <= purchased_grapes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purchased_grapes_premise'
    label = "contradiction"
elif purchased_mangoes_hypothesis!= purchased_mangoes_premise:
    # check if the number of mangoes in the hypothesis contradicts the number of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
