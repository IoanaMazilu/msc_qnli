visitors_friday_premise = 1250
visitors_saturday_premise = 416.666666667

# the hypothesis refers to the number of visitors on Saturday, which are also mentioned in the premise
# compute the number of visitors on Saturday from the premise
visitors_saturday_premise = visitors_friday_premise / 3
if visitors_saturday_hypothesis!= visitors_saturday_premise:
    # check if the number of visitors on Saturday from the hypothesis contradicts the number of visitors from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
