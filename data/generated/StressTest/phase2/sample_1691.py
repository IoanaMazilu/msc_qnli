# Premise: If Mel saved more than $10 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Hypothesis: If Mel saved more than $more than 10 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Golden Label: contradiction

saved_premise = 10
discount_premise = 15

saved_hypothesis = 10
discount_hypothesis = 15

# the premise and hypothesis are talking about the savings and discount on a sweater
if saved_hypothesis != saved_premise:
    # check if the savings mentioned in the hypothesis contradict the savings mentioned in the premise
    label = "contradiction"
elif discount_premise != discount_hypothesis:
    # check if the discount mentioned in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
else:
    # if all the mentioned values and conditions in the hypothesis match exactly with the premise, we can infer entailment
    label = "entailment"

print(label)

