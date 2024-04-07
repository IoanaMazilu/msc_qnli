# Premise: Adam spent 1/6 of his lifetime in adolescence.
# Hypothesis: Adam spent less than 1/6 of his lifetime in adolescence.
# Golden Label: contradiction

adolescence_time_premise = 1/6
adolescence_time_hypothesis = 1/6

# the hypothesis refers to the fraction of Adam's lifetime spent in adolescence mentioned in the premise
if adolescence_time_hypothesis >= adolescence_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

