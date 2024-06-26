tariffs_premise = 16
tariffs_hypothesis = 16

# the hypothesis and premise mention the amount of tariffs on Chinese goods
if tariffs_hypothesis!= tariffs_premise:
    # check if the amount of tariffs in the hypothesis contradicts the amount of tariffs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
