# Premise: more than 7 years ago Jason was 12 times older.
# Hypothesis: 8 years ago Jason was 12 times older.
# Golden Label: neutral

years_premise = 7
years_hypothesis = 8
times_older_premise = times_older_hypothesis = 12

# the hypothesis refers to the same time period and age proportion as the premise
if years_hypothesis > years_premise:
    # check if the number of 'years_hypothesis' contradicts the estimate of more than 'years_premise'
    label = "contradiction"
elif times_older_hypothesis != times_older_premise:
    # check if the age proportion in the hypothesis contradicts the age proportion in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

