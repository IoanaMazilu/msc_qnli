# Premise: Cases:159 deaths are thought to have been caused by swine flu, according to Jose Angel Cordova, Mexico's secretary of health.
# Hypothesis: More than 150 deaths in Mexico are thought to have been caused by swine flu.
# Golden Label: entailment

deaths_premise = 159
deaths_hypothesis = 150

# the hypothesis mentions the number of deaths caused by swine flu, which is also mentioned in the premise
if deaths_premise <= deaths_hypothesis:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the number of deaths in the hypothesis does not contradict the number of deaths in the premise, we can infer entailment
    label = "entailment"

print(label)

