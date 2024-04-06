# Premise: Google is hoping to make it a little simpler by providing easy-to-see nutrition info for more than 1,000 foods.
# Hypothesis: Google will showcase nutrition info for more than 1,000 foods in search.
# Golden Label: entailment

foods_premise = 1000
foods_hypothesis = 1000

# the hypothesis mentions the number of foods for which Google will provide nutritional information, which is also referenced in the premise
if foods_hypothesis != foods_premise:
    # check if the number of foods in the hypothesis contradicts the number given in the premise
    label = "contradiction"
else:
    # if the number of foods in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

