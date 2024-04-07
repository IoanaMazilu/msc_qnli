# Premise: Tarun got 30% concession on the labelled price of an article and sold it for Rs.
# Hypothesis: Tarun got more than 30% concession on the labelled price of an article and sold it for Rs.
# Golden Label: contradiction

concession_percentage_premise = 30
concession_percentage_hypothesis = 30

# the hypothesis talks about the concession percentage on the price of an article, also mentioned in the premise
if concession_percentage_hypothesis > concession_percentage_premise:
    # the hypothesis claims a concession percentage higher than the premise, which contradicts the premise
    label = "contradiction"
else:
    # if both the premise and hypothesis claim the same concession percentage, we can infer entailment
    label = "entailment"

print(label)

