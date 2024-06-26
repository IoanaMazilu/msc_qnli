cleaning_time_doubled_speed_premise = 3
cleaning_time_doubled_speed_hypothesis = 7

# both the hypothesis and the premise refer to the time it would take to clean their house if Anne's speed were doubled
if cleaning_time_doubled_speed_premise != cleaning_time_doubled_speed_hypothesis:
    # since the cleaning time in the hypothesis contradicts the cleaning time in the premise
    label = "contradiction"
else:
    # if the cleaning time in the hypothesis does not contradict the cleaning time in the premise
    label = "entailment"

print(label)
