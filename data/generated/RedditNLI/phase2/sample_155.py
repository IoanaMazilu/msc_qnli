# Premise: US economy sees weakest growth for three years in first quarter of 2017.
# Hypothesis: US Economy Expanded at Weakest Pace in Three Years.
# Golden Label: entailment

years_premise = 3
years_hypothesis = 3

# the hypothesis and premise mention the same number of years for the weakest growth of US economy
if years_premise != years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

