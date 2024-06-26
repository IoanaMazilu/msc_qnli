# Define the ratio of the area of triangle ADE to that of the trapezium DECB in the premise and hypothesis
ratio_premise = 144 / 25
ratio_hypothesis = 244 / 25

# Define the length of BC in the premise and hypothesis
length_bc_premise = 13
length_bc_hypothesis = 13

# Calculate the length of DE in the premise and hypothesis
length_de_premise = (ratio_premise * length_bc_premise) / 100
length_de_hypothesis = (ratio_hypothesis * length_bc_hypothesis) / 100

# Check if the length of DE in the hypothesis contradicts the length of DE in the premise
if length_de_hypothesis!= length_de_premise:
    label = "contradiction"
elif length_de_hypothesis < length_de_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
