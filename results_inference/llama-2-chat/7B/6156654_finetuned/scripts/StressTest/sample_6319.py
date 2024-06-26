apples_premise = 7
apples_hypothesis = 4
given_to_mike_premise = 2
given_to_mike_hypothesis = 2

# the hypothesis talks about the number of apples Maddie has, which is also mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the number of apples in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of apples in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
