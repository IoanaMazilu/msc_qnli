terrorists_premise = 700
terrorists_hypothesis = 700

# the hypothesis mentions the number of terrorists and their families that fled from Syria to Turkey
# the premise also mentions the same information
if terrorists_premise!= terrorists_hypothesis:
    # check if the number of terrorists in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of terrorists in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
