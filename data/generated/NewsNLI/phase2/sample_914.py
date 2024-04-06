# Premise: Holder said the Justice Department is working on extradition proceedings for the seven charged in the consulate killings and already in custody.
# Hypothesis: Ten Mexican nationals have been charged and seven are already in custody.
# Golden Label: neutral

charged_premise = 7
custody_premise = 7
charged_hypothesis = 10
custody_hypothesis = 7

# the hypothesis mentions the number of people charged and the number of people in custody, which are also mentioned in the premise
if charged_hypothesis != charged_premise:
    # check if the number of people charged in the hypothesis contradicts the number of people charged in the premise
    label = "contradiction"
elif custody_hypothesis != custody_premise:
    # check if the number of people in custody from the hypothesis contradicts the number of people in custody in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

