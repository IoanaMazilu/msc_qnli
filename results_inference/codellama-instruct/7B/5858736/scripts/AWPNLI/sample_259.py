# define variables for the distances driven by Darius and Julia
darius_miles = 679.0
julia_miles = 998.0

# compute the total number of miles driven by both Darius and Julia
total_miles = darius_miles + julia_miles

# check if the total number of miles driven by both Darius and Julia is equal to the hypothesis
if total_miles == 1672.0:
    label = "entailment"
else:
    label = "contradiction"

print(label)
