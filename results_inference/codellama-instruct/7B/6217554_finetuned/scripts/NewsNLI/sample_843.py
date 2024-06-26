lead_premise = 14
lead_hypothesis = 14

# the hypothesis mentions the lead of Mark Webber in the world championship race, which is also referenced in the premise
if lead_hypothesis!= lead_premise:
    # check if the lead in the hypothesis contradicts the lead reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
