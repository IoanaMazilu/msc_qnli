# Premise: Billy has 5 apples.
# Hypothesis: Billy has 4 apples.
# Golden Label: contradiction

apples_premise = 5
apples_hypothesis = 4

# the hypothesis talks about the number of apples Billy has, which is also mentioned in the premise
if apples_hypothesis == apples_premise:
    # check if the number of apples in the hypothesis is the same as mentioned in the premise
    label = "entailment"
elif apples_hypothesis != apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

