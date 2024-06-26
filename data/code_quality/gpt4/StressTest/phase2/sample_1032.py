shirts_bought_premise = 160
shirts_bought_hypothesis = 260

# the hypothesis talks about the number of shirts Vijay bought, referenced also in the premise
if shirts_bought_hypothesis <= shirts_bought_premise:
    # check if the hypothesis value contradicts the number of shirts Vijay bought in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
