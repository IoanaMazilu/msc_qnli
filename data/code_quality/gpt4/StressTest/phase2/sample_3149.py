reading_rate_premise = 3/5
reading_rate_hypothesis = 3/5

# the hypothesis refers to the reading rate of Ros é mentioned in the premise
if reading_rate_hypothesis >= reading_rate_premise:
    # check if the estimate of 'reading_rate_hypothesis' contradicts the reading rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
