# Premise: Adam spent 1/6 of his lifetime in adolescence.
# Hypothesis: Adam spent less than 6/6 of his lifetime in adolescence.
# Golden Label: entailment

lifetime_spent_adolescence_premise = 1/6
lifetime_spent_adolescence_hypothesis = 6/6

# the hypothesis talks about the fraction of Adam's lifetime spent in adolescence, referenced also in the premise
if lifetime_spent_adolescence_hypothesis <= lifetime_spent_adolescence_premise:
    # check if the hypothesis value contradicts the fraction of lifetime spent in adolescence in the premise
    label = "contradiction"
else:
    # the premise gives a specific fraction for the time spent in adolescence
    # any fraction of time less than 'lifetime_spent_adolescence_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

