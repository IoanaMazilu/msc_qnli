watermelons_left_premise = 536
watermelons_left_hypothesis = 136

# the hypothesis refers to the number of watermelons left after Sally left, which is also mentioned in the premise
if watermelons_left_hypothesis!= watermelons_left_premise:
    # check if the number of watermelons left in the hypothesis contradicts the number of watermelons left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
