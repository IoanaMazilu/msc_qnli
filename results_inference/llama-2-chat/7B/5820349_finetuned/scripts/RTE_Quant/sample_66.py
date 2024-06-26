official_languages_premise = 2
official_languages_hypothesis = 2

# the hypothesis talks about the number of official EU languages, which is also mentioned in the premise
if official_languages_hypothesis!= official_languages_premise:
    # check if the number of official languages in the hypothesis contradicts the number of official languages from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
