father_age_premise = 30
father_age_hypothesis = 50
mother_age_premise = 22
mother_age_hypothesis = 22

# the hypothesis talks about the ages of Ayesha's parents at the time of her and her brother's birth, referenced also in the premise
if father_age_premise > father_age_hypothesis:
    # check if the actual age of Ayesha's father at her birth contradicts the estimate of less than 'father_age_hypothesis'
    label = "contradiction"
elif mother_age_premise != mother_age_hypothesis:
    # check if the actual age of Ayesha's mother at the birth of Ayesha's brother contradicts the age reported in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
