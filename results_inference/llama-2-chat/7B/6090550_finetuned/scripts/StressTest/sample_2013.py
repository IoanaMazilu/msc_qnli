ryan_premise = 2
ryan_hypothesis = 6
interest_rate = 4

# the hypothesis refers to the number of years and the interest rate mentioned in the premise
if ryan_hypothesis!= ryan_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the number of years in the premise, we can infer entailment
    label = "entailment"

print(label)

