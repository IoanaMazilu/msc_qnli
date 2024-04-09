kiran_age_premise = 7 * 9 = 63
bineesh_age_premise = 9 * 9 = 81

# define variables for the hypothesis
kiran_age_hypothesis = 63 - 7
bineesh_age_hypothesis = 81 - 7

# compare the values of the premise and hypothesis
if kiran_age_hypothesis > kiran_age_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif bineesh_age_hypothesis > bineesh_age_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values are consistent with the premise
    label = "neutral"

print(label)
