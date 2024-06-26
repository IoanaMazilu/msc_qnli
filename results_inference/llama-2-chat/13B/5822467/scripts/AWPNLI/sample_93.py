eggs_premise = 47.0
eggs_taken_premise = 5.0
eggs_hypothesis = 41.0

# compute the number of eggs left in the premise
left_eggs_premise = eggs_premise - eggs_taken_premise

if eggs_hypothesis > left_eggs_premise:
    # check if the number of eggs left in the hypothesis contradicts the number of eggs left in the premise
    label = "contradiction"
elif eggs_hypothesis < left_eggs_premise:
    # check if the number of eggs left in the hypothesis is less than the number of eggs left in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
