# Premise: A new report claiming to be the most comprehensive look at global slavery says 30 million people are living as slaves around the world.
# Hypothesis: A new report claims 30 million people are living as slaves globally.
# Golden Label: entailment

slaves_premise = 30000000
slaves_hypothesis = 30000000

# the hypothesis mentions the number of people living as slaves globally, which is also referenced in the premise
if slaves_hypothesis != slaves_premise:
    # check if the number of people living as slaves globally in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the number of people living as slaves globally in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

