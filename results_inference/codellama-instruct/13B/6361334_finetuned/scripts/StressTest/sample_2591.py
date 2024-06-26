sameer_age_premise = 5
anand_age_premise = 4
sameer_age_hypothesis = 4
anand_age_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Sameer and Anand, which is also mentioned in the premise
if sameer_age_hypothesis >= sameer_age_premise:
    # check if the estimate of'sameer_age_hypothesis' contradicts the ratio of'sameer_age_premise'
    label = "contradiction"
elif anand_age_hypothesis >= anand_age_premise:
    # check if the estimate of 'anand_age_hypothesis' contradicts the ratio of 'anand_age_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
