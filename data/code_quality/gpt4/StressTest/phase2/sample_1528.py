parts_division_premise = 6
parts_division_hypothesis = 5

# the hypothesis refers to the number of parts that Cook can divide his herd into, mentioned also in the premise
if parts_division_hypothesis > parts_division_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parts_division_premise'
    label = "contradiction"
elif parts_division_hypothesis == parts_division_premise:
    # check if the number of parts in the hypothesis contradicts the number of parts mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
