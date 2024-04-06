# Premise: There have been three court hearings to consider challenges to the Arizona law, including one from the Department of Justice.
# Hypothesis: There are at least three court challenges to the law.
# Golden Label: entailment

hearings_premise = 3
hearings_hypothesis = 3

# the hypothesis mentions the number of court hearings which is also referenced in the premise
if hearings_hypothesis > hearings_premise:
    # check if the number of court hearings in the hypothesis contradicts the number of court hearings reported in the premise
    label = "contradiction"
else:
    # if the number of court hearings in the hypothesis does not contradict the number of court hearings in the premise, we can infer entailment
    label = "entailment"

print(label)

