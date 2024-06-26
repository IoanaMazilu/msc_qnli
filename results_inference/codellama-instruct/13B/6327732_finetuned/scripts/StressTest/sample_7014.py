lewis_age_premise = 1
brown_age_premise = 2
lewis_age_hypothesis = 6
brown_age_hypothesis = 2

# the hypothesis refers to the ratio of the ages of Lewis and Brown
if lewis_age_hypothesis < lewis_age_premise:
    # check if the estimate of 'lewis_age_hypothesis' contradicts the ratio of 'lewis_age_premise' and 'brown_age_premise'
    label = "contradiction"
elif brown_age_hypothesis!= brown_age_premise:
    # check if the estimate of 'brown_age_hypothesis' contradicts the ratio of 'lewis_age_premise' and 'brown_age_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
