webber_lead_premise = 14
webber_lead_hypothesis = 14

# the hypothesis mentions the lead of Mark Webber in the world title race, which is also mentioned in the premise
if webber_lead_hypothesis!= webber_lead_premise:
    # check if the lead in the hypothesis contradicts the lead reported in the premise
    label = "contradiction"
else:
    # if the lead in the hypothesis does not contradict the lead in the premise, we can infer entailment
    label = "entailment"

print(label)
