# Premise: Adam spent less than 6/6 of his lifetime in adolescence.
# Hypothesis: Adam spent 1/6 of his lifetime in adolescence.
# Golden Label: neutral

lifetime_adolescence_premise = 6/6
lifetime_adolescence_hypothesis = 1/6

# the hypothesis speaks about the fraction of Adam's lifetime spent in adolescence, which is also mentioned in the premise
if lifetime_adolescence_hypothesis >= lifetime_adolescence_premise:
    # check if the fraction in the hypothesis contradicts the estimate of less than 'lifetime_adolescence_premise'
    label = "contradiction"
elif lifetime_adolescence_hypothesis == lifetime_adolescence_premise:
    # check if the fraction in the hypothesis equals the fraction in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of lifetime spent in adolescence
    # any fraction less than 'lifetime_adolescence_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

