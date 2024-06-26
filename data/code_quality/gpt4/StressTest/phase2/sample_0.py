brothers_age_premise = 6
brothers_age_hypothesis = 1
rides_taken_premise = 3
rides_taken_hypothesis = 3

# the hypothesis talks about the age of Joe's brothers and the number of rides they took
if brothers_age_hypothesis >= brothers_age_premise:
    # check if the estimate of 'brothers_age_hypothesis' contradicts the age of brothers in the premise
    label = "contradiction"
elif rides_taken_hypothesis != rides_taken_premise:
    # check if the number of rides taken in the hypothesis contradicts the number of rides taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
