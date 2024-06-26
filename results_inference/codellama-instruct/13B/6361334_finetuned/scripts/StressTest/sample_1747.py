sameer_age_premise = 1
anand_age_premise = 4
sameer_age_hypothesis = 5
anand_age_hypothesis = 4

# the hypothesis refers to the ratio of the ages of Sameer and Anand, which is also mentioned in the premise
if sameer_age_hypothesis / anand_age_hypothesis <= sameer_age_premise / anand_age_premise:
    # check if the estimate of'sameer_age_hypothesis' and 'anand_age_hypothesis' contradicts the ratio of'sameer_age_premise' and 'anand_age_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
