double_speed_premise = 2
double_speed_hypothesis = 0.5
house_cleaning_time_premise = 3
house_cleaning_time_hypothesis = 5

# the hypothesis refers to the time it would take to clean the house if Anne's speed was doubled, mentioned in the premise
if double_speed_hypothesis >= double_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'double_speed_premise'
    label = "contradiction"
elif house_cleaning_time_hypothesis < house_cleaning_time_premise:
    # check if the time it would take to clean the house in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
