house_cleaning_time_premise = 4
house_cleaning_time_hypothesis = 3

# the hypothesis refers to the number of hours needed to clean the house, also mentioned in the premise
if house_cleaning_time_hypothesis!= house_cleaning_time_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
