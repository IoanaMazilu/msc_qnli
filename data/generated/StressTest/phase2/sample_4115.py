# Premise: 8 years ago Jason was 12 times older.
# Hypothesis: 7 years ago Jason was 12 times older.
# Golden Label: contradiction

years_ago_premise = 8
years_ago_hypothesis = 7
older_times_premise = 12
older_times_hypothesis = 12

# the hypothesis talks about the number of years ago when Jason was a certain times older, referenced also in the premise
if years_ago_hypothesis != years_ago_premise:
    # check if the number of years ago in the hypothesis contradicts the number of years ago reported in the premise
    label = "contradiction"
elif older_times_hypothesis != older_times_premise:
    # check if the number of times older Jason was in the hypothesis contradicts the number of times older Jason was reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

