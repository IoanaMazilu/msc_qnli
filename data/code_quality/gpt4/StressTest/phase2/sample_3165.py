borrowed_premise = 6000
borrowed_hypothesis = 1000

# the hypothesis refers to the total amount borrowed by Albert from Brian and Milton
if borrowed_hypothesis >= borrowed_premise:
    # check if the hypothesis value contradicts the total amount borrowed in the premise
    label = "contradiction"
elif borrowed_hypothesis > borrowed_premise:
    # the hypothesis specifies a minimum threshold for the borrowed amount
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
