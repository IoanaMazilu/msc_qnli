watermelons_premise = 536
watermelons_hypothesis = 136

# the hypothesis refers to the number of watermelons left after Sally left
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of 'watermelons_premise'
    label = "contradiction"
elif watermelons_premise!= watermelons_hypothesis:
    # check if the number of watermelons in the hypothesis contradicts the number of watermelons reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
