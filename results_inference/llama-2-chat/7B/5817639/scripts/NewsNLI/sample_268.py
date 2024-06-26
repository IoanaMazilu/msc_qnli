ministry_premise = "Indonesia's Ministry of Transport"
airasia_premise = "AirAsia"
investigation_hypothesis = "full investigation"
suspension_hypothesis = "suspend"

# compare the hypothesis with the premise
if investigation_hypothesis!= ministry_premise or suspension_hypothesis!= airasia_premise:
    # check if the investigation and suspension in the hypothesis contradict the ministry and airline in the premise
    label = "contradiction"
else:
    # if the hypothesis values and entities do not contradict the premise values and entities, we can infer entailment
    label = "entailment"

print(label)
