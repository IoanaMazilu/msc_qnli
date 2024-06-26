fine_premise = 480350  # fine in dollars imposed on the firm
fine_hypothesis = 0.5e6  # "nearly half million dollar" fine referred in the hypothesis

# the hypothesis talks about the fine imposed on a firm, which is also mentioned in the premise
# we need to check if the fine value in the hypothesis contradicts the fine value from the premise
if fine_hypothesis > fine_premise:
    label = "contradiction"
else:
    # if the fine value in the hypothesis does not contradict the fine from the premise, we can infer entailment
    label = "entailment"

print(label)
