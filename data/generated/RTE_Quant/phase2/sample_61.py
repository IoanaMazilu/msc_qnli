# Premise: This is good news for Gaelic translators, as the EU will have to churn out official documents in this language, in addition to the 20 other official EU languages.
# Hypothesis: There are 21 official EU languages.
# Golden Label: entailment

official_languages_premise = 20
official_languages_hypothesis = 21

# the hypothesis talks about the total number of official EU languages, which is also mentioned in the premise
# but the premise provides information about the languages before the addition of Gaelic
# so we add 1 to the official_languages_premise to account for the addition of Gaelic
official_languages_premise += 1

if official_languages_hypothesis == official_languages_premise:
    # if the number of official EU languages in the hypothesis is equal to the number of official EU languages in the premise
    # after the addition of Gaelic, we can infer entailment
    label = "entailment"
else:
    # if the number of official EU languages in the hypothesis is not equal to the number of official EU languages in the premise
    # after the addition of Gaelic, we infer contradiction
    label = "contradiction"

print(label)

