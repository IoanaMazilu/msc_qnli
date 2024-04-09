bruce_cleaning_rate_premise = 1/4
anne_cleaning_rate_premise = 1/4
house_cleaning_time_premise = 4

# define variables for the hypothesis
bruce_cleaning_rate_hypothesis = 1/3
anne_cleaning_rate_hypothesis = 1/3
house_cleaning_time_hypothesis = 3

# check if the hypothesis contradicts the premise
if bruce_cleaning_rate_hypothesis * house_cleaning_time_hypothesis > bruce_cleaning_rate_premise * house_cleaning_time_premise:
    label = "contradiction"
elif anne_cleaning_rate_hypothesis * house_cleaning_time_hypothesis > anne_cleaning_rate_premise * house_cleaning_time_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
