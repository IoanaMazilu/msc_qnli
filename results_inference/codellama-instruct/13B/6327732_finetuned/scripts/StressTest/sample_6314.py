num_males_premise = 4
num_females_premise = 3
num_males_hypothesis = 5
num_females_hypothesis = 4

# the hypothesis refers to the number of males and females mentioned in the premise
if num_males_hypothesis <= num_males_premise and num_females_hypothesis <= num_females_premise:
    # check if the hypothesis values contradict the number of males and females in the premise
    label = "contradiction"
elif num_males_hypothesis > num_males_premise or num_females_hypothesis > num_females_premise:
    # check if the hypothesis values contradict the number of males and females in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
