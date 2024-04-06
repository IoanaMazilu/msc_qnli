# Premise: The American Nonsmokers'Rights Foundation reports nearly 60 college campuses around the United States have smoke-free policies that affect the entire campus.
# Hypothesis: Nearly 60 U.S. colleges have smoke-free policies that affect entire campus.
# Golden Label: entailment

smoke_free_campuses_premise = 60
smoke_free_campuses_hypothesis = 60

# the hypothesis mentions the number of smoke-free campuses in the U.S., which is also mentioned in the premise
if smoke_free_campuses_hypothesis != smoke_free_campuses_premise:
    # check if the number of smoke-free campuses in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of smoke-free campuses in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

