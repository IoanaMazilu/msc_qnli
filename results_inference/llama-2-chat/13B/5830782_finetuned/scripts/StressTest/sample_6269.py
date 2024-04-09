died_premise = 10
died_hypothesis = 10
left_premise = 20
left_hypothesis = 20

# the hypothesis refers to the percentage of people who died and left in a village, mentioned in the premise
if died_hypothesis <= died_premise:
    # check if the estimate of 'died_hypothesis' contradicts the percentage of died people in the premise
    label = "contradiction"
elif left_hypothesis!= left_premise:
    # check if the percentage of people who left in the hypothesis contradicts the percentage of people who left reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
