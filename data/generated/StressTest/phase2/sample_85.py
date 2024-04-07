# Premise: In Richard's office one half of the workers are Indians, quarter are from America, one-fifth are from Canada and the other less than 300 are China.
# Hypothesis: In Richard's office one half of the workers are Indians, quarter are from America, one-fifth are from Canada and the other 100 are China.
# Golden Label: neutral

china_workers_premise = 300
china_workers_hypothesis = 100

# the hypothesis refers to the number of Chinese workers in Richard's office mentioned in the premise
if china_workers_hypothesis > china_workers_premise:
    # check if the number of Chinese workers in the hypothesis contradicts the number of Chinese workers in the premise
    label = "contradiction"
elif china_workers_hypothesis == china_workers_premise:
    # check if the number of Chinese workers in the hypothesis equals the number of Chinese workers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

