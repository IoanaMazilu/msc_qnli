# Premise: 1,250 people visited the zoo on Friday and 3 times as many people visited on Friday than on Saturday.
# Hypothesis: 416.666666667 people visited the zoo on Saturday.
# Golden Label: entailment

friday_visitors_premise = 1250
saturday_visitors_hypothesis = 416.666666667

# the hypothesis refers to the number of visitors on Saturday, which can be inferred from the premise
# compute the number of visitors on Saturday from the premise
saturday_visitors_premise = friday_visitors_premise / 3
if saturday_visitors_hypothesis != saturday_visitors_premise:
    # check if the number of Saturday visitors in the hypothesis contradicts the number of Saturday visitors from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

