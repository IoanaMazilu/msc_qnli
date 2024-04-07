# Premise: The ratio of the ages of Hema and Her brother is 3:2.
# Hypothesis: The ratio of the ages of Hema and Her brother is less than 8:2.
# Golden Label: entailment

hema_brother_ratio_premise = 3/2
hema_brother_ratio_hypothesis = 8/2

# the hypothesis refers to the ratio of ages of Hema and her brother mentioned in the premise
if hema_brother_ratio_hypothesis < hema_brother_ratio_premise:
    # check if the 'hema_brother_ratio_hypothesis' contradicts the ratio given in the premise
    label = "contradiction"
elif hema_brother_ratio_hypothesis == hema_brother_ratio_premise:
    # if the hypothesis ratio equals the ratio from the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a specific ratio for the ages of Hema and her brother
    # any ratio greater than 'hema_brother_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

