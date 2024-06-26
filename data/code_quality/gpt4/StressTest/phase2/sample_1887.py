matthews_rate_premise = 3
johnnys_rate_premise = 4
matthews_rate_hypothesis = 4
johnnys_rate_hypothesis = 4

# the hypothesis talks about Matthew's and Johnny's walking rates, which are also mentioned in the premise
if matthews_rate_premise >= matthews_rate_hypothesis:
    # check if the hypothesis estimate contradicts Matthew's walking rate in the premise
    label = "contradiction"
elif johnnys_rate_premise != johnnys_rate_hypothesis:
    # check if the hypothesis value contradicts Johnny's walking rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
