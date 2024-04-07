# Premise: Jeevan bought an article with 30 per cent discount on the labelled price.
# Hypothesis: Jeevan bought an article with more than 20 per cent discount on the labelled price.
# Golden Label: entailment

discount_premise = 30
discount_hypothesis = 20

# the hypothesis refers to the discount percentage on the article mentioned in the premise
if discount_premise < discount_hypothesis:
    # check if the discount in the premise contradicts the discount estimate in the hypothesis
    label = "contradiction"
else:
    # if the premise discount does not contradict the hypothesis discount, we can infer entailment
    label = "entailment"

print(label)

