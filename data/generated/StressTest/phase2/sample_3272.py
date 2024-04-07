# Premise: Tom alone cleans the entire house in 6 hours.
# Hypothesis: Tom alone cleans the entire house in less than 6 hours.
# Golden Label: contradiction

cleaning_time_premise = 6
cleaning_time_hypothesis = 6

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis of 'less than cleaning_time_hypothesis' contradicts the cleaning time in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

