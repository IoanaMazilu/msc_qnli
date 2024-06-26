cans_premise = 6
cans_hypothesis = 7

# the hypothesis refers to the number of cans of paint Diane used to paint one third of her room
if cans_hypothesis <= cans_premise:
    # check if the hypothesis value contradicts the number of cans stated in the premise
    label = "contradiction"
elif cans_hypothesis != cans_premise + 1:
    # check if the number of cans in the hypothesis is more than the number of cans used in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
