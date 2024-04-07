# Premise: If Tim hires this freelancer, and hires him again to make alterations which took 20 more hours.
# Hypothesis: If Tim hires this freelancer, and hires him again to make alterations which took less than 80 more hours.
# Golden Label: entailment

alterations_duration_premise = 20
alterations_duration_hypothesis = 80

# the hypothesis refers to the duration of some alterations mentioned in the premise
if alterations_duration_hypothesis < alterations_duration_premise:
    # check if the estimate of 'alterations_duration_hypothesis' contradicts the duration of alterations in the premise
    label = "contradiction"
elif alterations_duration_hypothesis == alterations_duration_premise:
    # check if the duration of alterations in the hypothesis exactly matches the duration of alterations reported in the premise
    label = "entailment"
else:
    # the premise gives a specific duration for the alterations
    # any duration of alterations less than 'alterations_duration_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

