# Define variables for the premise and hypothesis
premise_land_area = 120
hypothesis_land_area = 320

# Check if the hypothesis is a contradiction to the premise
if hypothesis_land_area > premise_land_area:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
