# define variables with representative names for the numerical entities in both inputs
anne_speed_premise = 2
anne_speed_hypothesis = 4
house_cleaning_time_premise = 3
house_cleaning_time_hypothesis = 5

# extract all quantities as valid numbers (integers or floats)
house_cleaning_time_premise = int(house_cleaning_time_premise)
house_cleaning_time_hypothesis = int(house_cleaning_time_hypothesis)
anne_speed_premise = int(anne_speed_premise)
anne_speed_hypothesis = int(anne_speed_hypothesis)

# perform calculations if necessary
house_cleaning_time_doubled = house_cleaning_time_hypothesis * 2

# compare the variables
if anne_speed_premise <= anne_speed_hypothesis:
    # check if the estimate of 'anne_speed_hypothesis' contradicts the value of 'anne_speed_premise'
    label = "contradiction"
elif house_cleaning_time_premise!= house_cleaning_time_doubled:
    # check if the number of hours needed to clean the house in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
