# Premise: Billy has 12 apples.
# Hypothesis: Billy has less than 72 apples.
# Golden Label: entailment

apples_billy_premise = 12
apples_billy_hypothesis = 72

# the hypothesis talks about the number of apples Billy has, which is also mentioned in the premise
if apples_billy_premise >= apples_billy_hypothesis:
    # check if the exact number of 'apples_billy_premise' contradicts the hypothesis estimate of less than 'apples_billy_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

