first_set_premise = 2
second_set_premise = 6
third_set_premise = 6

first_set_hypothesis = 2
second_set_hypothesis = 6
third_set_hypothesis = 6

# the hypothesis mentions the score of the match, which is also mentioned in the premise
if first_set_hypothesis != first_set_premise:
    # check if the score of the first set in the hypothesis contradicts the score of the first set reported in the premise
    label = "contradiction"
elif second_set_hypothesis != second_set_premise:
    # check if the score of the second set from the hypothesis contradicts the score of the second set in the premise
    label = "contradiction"
elif third_set_hypothesis != third_set_premise:
    # check if the score of the third set from the hypothesis contradicts the score of the third set in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
