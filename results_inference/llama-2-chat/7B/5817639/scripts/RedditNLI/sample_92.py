fine_premise = 1400000000
fine_hypothesis = 1400000000

# the premise mentions a specific fine imposed on Deutsche Bank
# the hypothesis mentions the same fine, but with a different wording
if fine_hypothesis == fine_premise:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "entailment"
elif fine_hypothesis < fine_premise:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "contradiction"
else:
    # the fine in the hypothesis does not contradict the fine in the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
