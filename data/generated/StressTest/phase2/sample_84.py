# Premise: In Richard's office one half of the workers are Indians, quarter are from America, one-fifth are from Canada and the other 100 are China.
# Hypothesis: In Richard's office one half of the workers are Indians, quarter are from America, one-fifth are from Canada and the other less than 300 are China.
# Golden Label: entailment

china_workers_premise = 100
china_workers_hypothesis = 300

# the hypothesis talks about the number of Chinese workers in Richard's office, referenced also in the premise
if china_workers_hypothesis < china_workers_premise:
    # check if the hypothesis value contradicts the exact number of Chinese workers in the premise
    label = "contradiction"
elif china_workers_hypothesis == china_workers_premise:
    # if the hypothesis value equals the number of Chinese workers in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives the exact number of Chinese workers
    # any number of Chinese workers greater than 'china_workers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

