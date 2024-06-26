# Define the variables for the premise and hypothesis
percentage_boys_premise = 30
percentage_boys_hypothesis = 10

# The hypothesis refers to the percentage of boys at Jones Elementary School, which is also mentioned in the premise
if percentage_boys_premise <= percentage_boys_hypothesis:
    # Check if the percentage of boys in the hypothesis contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the percentage of boys
    # Any percentage of boys greater than 'percentage_boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)