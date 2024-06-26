judges_premise = 8
judges_hypothesis = 11

# the hypothesis mentions the number of judges in the Yugoslavia war tribunal, which is also mentioned in the premise
# however, the hypothesis adds a detail that is not mentioned in the premise (the year)
if judges_hypothesis!= judges_premise:
    # check if the number of judges in the hypothesis contradicts the number of judges in the premise
    label = "contradiction"
else:
    # if the number of judges in the hypothesis does not contradict the number of judges in the premise, we can infer entailment
    label = "entailment"

print(label)
