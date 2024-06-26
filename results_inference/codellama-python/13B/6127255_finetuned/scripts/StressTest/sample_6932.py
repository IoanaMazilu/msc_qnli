years_future_premise = 6
age_future_premise = 30
years_future_hypothesis = 6
age_future_hypothesis = 30

# the hypothesis refers to the same future age of Sandy mentioned in the premise
if years_future_hypothesis >= years_future_premise and age_future_hypothesis == age_future_premise:
    # check if the hypothesis contradicts the premise by stating a number of years ahead that is greater or equal to the number of years in the premise
    # and if the future age is the same
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
