official_languages_premise = 2
official_languages_hypothesis = 2

# the hypothesis talks about the number of official languages in the EU, which is also mentioned in the premise
if official_languages_hypothesis == official_languages_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
elif official_languages_hypothesis < official_languages_premise:
    # if the number of official languages in the hypothesis is less than the number in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values do not contradict each other, we can infer neutrality
    label = "neutral"

print(label)
