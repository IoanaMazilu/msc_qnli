sailors_premise = 3
sailors_hypothesis = 3

# the hypothesis mentions the number of sailors who are unharmed and back aboard, which is also mentioned in the premise
if sailors_hypothesis!= sailors_premise:
    # check if the number of sailors in the hypothesis contradicts the number of sailors in the premise
    label = "contradiction"
else:
    # if the number of sailors in the hypothesis does not contradict the number of sailors in the premise, we can infer entailment
    label = "entailment"

print(label)
