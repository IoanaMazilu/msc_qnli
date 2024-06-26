# Define variables for the sides of the triangle
sides_st = 26
sides_tv = 26
sides_sv = 20

# Check if the hypothesis is entailed from the premise
if sides_st < 26 and sides_tv < 26 and sides_sv == 20:
    label = "entailment"
else:
    label = "contradiction"

print(label)
