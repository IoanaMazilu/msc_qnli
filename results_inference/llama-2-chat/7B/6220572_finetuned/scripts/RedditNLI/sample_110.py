percentage_change_premise = 1.5
percentage_change_hypothesis = 1.5

# the hypothesis and premise mention the percentage change in pending sales of homes
# the premise gives the percentage change in one month, the hypothesis gives the same percentage change in another month
if percentage_change_hypothesis!= percentage_change_premise:
    # check if the percentage change in the hypothesis contradicts the percentage change in the premise
    label = "contradiction"
else:
    # if the premise and hypothesis values do not contradict, we can infer entailment
    label = "entailment"

print(label)
