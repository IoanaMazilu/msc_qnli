wounded_premise = 1000
wounded_hypothesis = 6000
killed_premise = 1
killed_hypothesis = 6

# the hypothesis mentions the number of wounded and killed, which are also mentioned in the premise
# however, the hypothesis mentions a higher number of wounded and killed, which cannot be entailed from the premise
if wounded_hypothesis!= wounded_premise:
    # check if the number of wounded in the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
elif killed_hypothesis!= killed_premise:
    # check if the number of killed in the hypothesis contradicts the number of killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
