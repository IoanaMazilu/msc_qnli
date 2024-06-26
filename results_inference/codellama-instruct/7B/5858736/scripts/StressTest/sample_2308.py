# Define variables for the numerical entities in the premise and hypothesis
premise_anne_speed = 2
premise_cleaning_time = 5
premise_house_cleaning_rate = 1

hypothesis_anne_speed = 4
hypothesis_cleaning_time = 3
hypothesis_house_cleaning_rate = 1

# Calculate the cleaning time for the premise and hypothesis
premise_cleaning_time_doubled = premise_anne_speed * premise_cleaning_time
hypothesis_cleaning_time_doubled = hypothesis_anne_speed * hypothesis_cleaning_time

# Compare the cleaning times for the premise and hypothesis
if premise_cleaning_time_doubled <= hypothesis_cleaning_time_doubled:
    # The hypothesis cleaning time is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
elif premise_cleaning_time_doubled > hypothesis_cleaning_time_doubled:
    # The hypothesis cleaning time contradicts the premise
    label = "contradiction"
else:
    # The hypothesis cleaning time is less than the premise, but cannot be explicitly entailed from the premise
    label = "contradiction"

print(label)
