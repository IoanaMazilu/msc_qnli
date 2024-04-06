# Premise: This is good news for Gaelic translators, as the EU will have to churn out official documents in this language, in addition to the 20 other official EU languages.
# Hypothesis: There are 20 official EU languages.
# Golden Label: neutral

official_languages_premise = 20
official_languages_hypothesis = 20

# the hypothesis talks about the number of official EU languages, which is also mentioned in the premise
if official_languages_hypothesis != official_languages_premise:
    # check if the number of official EU languages in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

