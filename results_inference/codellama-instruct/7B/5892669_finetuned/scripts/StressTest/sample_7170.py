problems_start_premise = 70
problems_end_premise = 125
problems_start_hypothesis = 30
problems_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_start_hypothesis < problems_start_premise:
    # check if the start of the problem range in the hypothesis contradicts the start of the problem range in the premise
    label = "contradiction"
elif problems_end_hypothesis!= problems_end_premise:
    # check if the end of the problem range in the hypothesis contradicts the end of the problem range in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
