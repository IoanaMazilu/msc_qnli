# Premise: Billy has 6 apples.
# Hypothesis: Billy has more than 6 apples.
# Golden Label: contradiction

apples_billy_premise = 6
apples_billy_hypothesis = 6

# the hypothesis talks about the number of apples Billy has, also mentioned in the premise
if apples_billy_hypothesis >= apples_billy_premise:
    # check if the hypothesis value contradicts the exact number 'apples_billy_premise' mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise's exact number, then the premise can explicitly entail the hypothesis
    label = "entailment"

print(label)

