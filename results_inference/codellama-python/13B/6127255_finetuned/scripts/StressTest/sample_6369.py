cans_premise = 4
cans_hypothesis = 8

# the hypothesis refers to the number of cans of paint Diane used to paint one third of her room
if cans_premise >= cans_hypothesis:
    # check if the number of cans in the premise contradicts the estimate of less than 'cans_hypothesis'
    label = "contradiction"
else:
    # if the premise number of cans does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
