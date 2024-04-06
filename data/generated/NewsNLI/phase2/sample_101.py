# Premise: Sarah Shourd, like the other two hikers, is a graduate of the University of California, Berkeley.
# Hypothesis: All three are graduates of University of California, Berkeley.
# Golden Label: entailment

graduates_premise = 3
graduates_hypothesis = 3

# the hypothesis mentions the number of graduates from University of California, Berkeley, which is also mentioned in the premise
if graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates mentioned in the premise
    label = "contradiction"
else:
    # if the number of graduates in the hypothesis does not contradict the number mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

