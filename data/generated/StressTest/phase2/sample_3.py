# Premise: Tim has 350 pounds of cement in 100, 50, and 25 pound bags.
# Hypothesis: Tim has less than 750 pounds of cement in 100, 50, and 25 pound bags.
# Golden Label: entailment

cement_premise = 350
cement_hypothesis = 750

# the hypothesis refers to the weight of the cement mentioned in the premise
if cement_premise >= cement_hypothesis:
    # check if the premise value contradicts the estimate of less than 'cement_hypothesis'
    label = "contradiction"
elif cement_hypothesis <= cement_premise:
    # check if the hypothesis value contradicts the exact weight of the cement in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

