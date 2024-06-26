# Define variables for the numerical entities in the premise and hypothesis
premise_palestinian_demonstration = 2
premise_israeli_counter_demonstration = 25
premise_same_hours = True

hypothesis_israeli_demonstration = True
hypothesis_palestinian_counter_demonstration = 25

# Check if the hypothesis values and estimates do not contradict the premise values
if hypothesis_israeli_demonstration!= premise_israeli_counter_demonstration:
    label = "contradiction"
elif hypothesis_palestinian_counter_demonstration!= premise_palestinian_demonstration:
    label = "contradiction"
elif premise_same_hours!= True:
    label = "contradiction"
else:
    label = "entailment"

print(label)
