# Premise: Vijay sells a cupboard at 12% below cost price.
# Hypothesis: Vijay sells a cupboard at less than 62% below cost price.
# Golden Label: entailment

discount_premise = 12
discount_hypothesis = 62

# the hypothesis refers to the discount rate applied by Vijay when selling a cupboard, which is also mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount rate provided in the premise
    label = "contradiction"
elif discount_premise != discount_hypothesis:
    # check if the discount rate in the hypothesis contradicts the discount rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

