# Define variables for the sides of the triangle
sides_st = 26
sides_tv = 26
sides_sv = 20

# Define variables for the hypothesis
sides_st_hyp = 66
sides_tv_hyp = 66
sides_sv_hyp = 20

# Check if the hypothesis values contradict the premise
if sides_st_hyp > sides_st or sides_tv_hyp > sides_tv:
    label = "contradiction"
elif sides_sv_hyp!= sides_sv:
    label = "contradiction"
else:
    label = "neutral"

print(label)
