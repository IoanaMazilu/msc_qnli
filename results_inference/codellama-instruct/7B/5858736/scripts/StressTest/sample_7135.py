# Define variables for the sides of the triangle
sides_st = 10
sides_tv = 10
sides_sv = 12

# Define variables for the premise
sides_st_premise = 50
sides_tv_premise = 50
sides_sv_premise = 12

# Check if the hypothesis values contradict the premise
if sides_st!= sides_st_premise or sides_tv!= sides_tv_premise or sides_sv!= sides_sv_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
