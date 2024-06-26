premise = "If X, Y and Z are digits and more than 5 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"
hypothesis = "If X, Y and Z are digits and 7 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"

# extract the numerical entities from the premise and hypothesis
premise_entities = premise.split(" ")
hypothesis_entities = hypothesis.split(" ")

# define variables for the numerical entities
premise_x = premise_entities[0]
premise_y = premise_entities[1]
premise_z = premise_entities[2]
premise_xyz = premise_entities[3]

hypothesis_x = hypothesis_entities[0]
hypothesis_y = hypothesis_entities[1]
hypothesis_z = hypothesis_entities[2]
hypothesis_xyz = hypothesis_entities[3]

# perform calculations
premise_xyz_value = premise_x * premise_y * premise_z
hypothesis_xyz_value = hypothesis_x * hypothesis_y * hypothesis_z

# compare the values
if premise_xyz_value > hypothesis_xyz_value:
    label = "entailment"
elif premise_xyz_value < hypothesis_xyz_value:
    label = "contradiction"
else:
    label = "neutral"

print(label)
