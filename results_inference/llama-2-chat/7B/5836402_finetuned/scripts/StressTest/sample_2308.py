# define variables for the premise and hypothesis
doubled_speed_premise = 2
doubled_speed_hypothesis = 2
house_cleaning_time_premise = 5
house_cleaning_time_hypothesis = 3

# the hypothesis refers to the same aspect as the premise, so we can compare them directly
if doubled_speed_hypothesis!= doubled_speed_premise:
    # check if the doubled speed in the hypothesis contradicts the premise
    label = "contradiction"
elif house_cleaning_time_hypothesis!= house_cleaning_time_premise:
    # check if the house cleaning time in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
