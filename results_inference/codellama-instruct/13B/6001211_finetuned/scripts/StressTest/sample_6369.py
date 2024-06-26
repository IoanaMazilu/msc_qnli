cans_premise = 4
cans_hypothesis = 8

# the hypothesis refers to the number of cans of paint needed to paint one third of the room, mentioned in the premise
if cans_premise >= cans_hypothesis:
    # check if the number of cans in the premise contradicts the estimate of less than 'cans_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
