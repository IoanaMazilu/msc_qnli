# Premise: Tarun got 30% concession on the labelled price of an article and sold it for Rs.
# Hypothesis: Tarun got less than 80% concession on the labelled price of an article and sold it for Rs.
# Golden Label: entailment

concession_premise = 30
concession_hypothesis = 80

# the hypothesis refers to the concession percentage Tarun got, which is also mentioned in the premise
if concession_premise >= concession_hypothesis:
    # check if the 'concession_premise' contradicts the estimate of less than 'concession_hypothesis'
    label = "contradiction"
else:
    # if the 'concession_premise' does not contradict the 'concession_hypothesis', we can infer entailment
    label = "entailment"

print(label)

