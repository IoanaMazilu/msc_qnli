# Premise: Sharper is wanted in New Orleans in connection with the alleged rapes of two women.
# Hypothesis: The former NFL star faces two counts of aggravated rape in New Orleans.
# Golden Label: neutral

alleged_rapes_premise = 2
counts_of_rape_hypothesis = 2

# the hypothesis mentions the number of counts of rape, which is also mentioned in the premise
if counts_of_rape_hypothesis != alleged_rapes_premise:
    # check if the number of counts of rape in the hypothesis contradicts the number of alleged rapes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

