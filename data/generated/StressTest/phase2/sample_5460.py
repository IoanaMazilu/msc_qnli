# Premise: Billy has 5 apples.
# Hypothesis: Billy has more than 1 apples.
# Golden Label: entailment

apples_premise = 5
apples_hypothesis = 1

# the hypothesis refers to the number of apples mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the 'apples_hypothesis' contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the 'apples_hypothesis' does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

