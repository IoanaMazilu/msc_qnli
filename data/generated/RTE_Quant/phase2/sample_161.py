# Premise: Gemayel's assassination is almost certain to deepen the political crisis in Lebanon, which started after the resignation of six pro-Syrian ministers, two from Hezbollah, hours after all-party round table talks collapsed.
# Hypothesis: After the resignation of six pro-Syrian ministers a deep political crises started in Lebanon.
# Golden Label: entailment

resignation_ministers_premise = 6
resignation_ministers_hypothesis = 6

# the hypothesis and premise both mention the resignation of a certain number of pro-Syrian ministers
if resignation_ministers_premise != resignation_ministers_hypothesis:
    # check if the number of resignations in the hypothesis contradicts the number of resignations in the premise
    label = "contradiction"
else:
    # if the number of resignations in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

