age_premise = 23
has_leukemia_premise = False

# define variables for the hypothesis
age_hypothesis = 23
has_leukemia_hypothesis = True

# extract numerical information from the premise and hypothesis
if age_premise == age_hypothesis:
    # the hypothesis mentions the same age as the premise, no contradiction
    label = "neutral"
elif has_leukemia_premise!= has_leukemia_hypothesis:
    # the hypothesis mentions having leukemia, which contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but cannot be fully entailed
    label = "neutral"

print(label)
