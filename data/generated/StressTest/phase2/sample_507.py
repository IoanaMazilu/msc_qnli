# Premise: A case of candy usually lasts Tomi 42 days when she eats 6 every day.
# Hypothesis: A case of candy usually lasts Tomi less than 62 days when she eats 6 every day.
# Golden Label: entailment

candy_duration_premise = 42
candy_duration_hypothesis = 62
candy_per_day = 6

# the hypothesis speaks about the duration a case of candy lasts for Tomi when she eats 'candy_per_day', a situation also described in the premise
if candy_duration_hypothesis <= candy_duration_premise:
    # check if the hypothesis estimate contradicts the duration in the premise
    label = "contradiction"
elif candy_duration_hypothesis > candy_duration_premise:
    # any duration longer than 'candy_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis estimate does not contradict the premise duration, we can infer entailment
    label = "entailment"

print(label)

