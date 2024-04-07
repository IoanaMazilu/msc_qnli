# Premise: Shreehari has 125 pencils.
# Hypothesis: Shreehari has less than 425 pencils.
# Golden Label: entailment

pencils_premise = 125
pencils_hypothesis = 425

# the hypothesis refers to the number of pencils Shreehari has, mentioned in the premise
if pencils_premise >= pencils_hypothesis:
    # check if the actual number of pencils in the premise contradicts the estimate of less than 'pencils_hypothesis'
    label = "contradiction"
else:
    # the number of pencils in the premise is less than 'pencils_hypothesis', hence it doesn't contradict it
    # since the exact number of pencils is known from the premise, we can infer entailment
    label = "entailment"

print(label)

