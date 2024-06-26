# define variables for the numerical entities in the premise and hypothesis
premise_hours_per_day_mon = 2
premise_hours_per_day_wed = 2
premise_hours_per_day_fri = 2
premise_hours_per_day_tue = 5
premise_hours_per_day_thu = 5

hypothesis_hours_per_day_mon = 9
hypothesis_hours_per_day_wed = 9
hypothesis_hours_per_day_fri = 9
hypothesis_hours_per_day_tue = 5
hypothesis_hours_per_day_thu = 5

# check if the hypothesis values contradict the premise values
if hypothesis_hours_per_day_mon!= premise_hours_per_day_mon or \
   hypothesis_hours_per_day_wed!= premise_hours_per_day_wed or \
   hypothesis_hours_per_day_fri!= premise_hours_per_day_fri or \
   hypothesis_hours_per_day_tue!= premise_hours_per_day_tue or \
   hypothesis_hours_per_day_thu!= premise_hours_per_day_thu:
    label = "contradiction"
else:
    label = "entailment"

print(label)
