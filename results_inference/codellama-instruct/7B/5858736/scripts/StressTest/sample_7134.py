# Define variables for the sides of the triangle
sides_st = 10
sides_tv = 10
sides_sv = 12

# Define variables for the hypothesis
sides_st_hyp = 50
sides_tv_hyp = 50
sides_sv_hyp = 12

# Check if the sides of the triangle in the hypothesis contradict the premise
if sides_st_hyp > sides_st or sides_tv_hyp > sides_tv:
    label = "contradiction"
elif sides_sv_hyp!= sides_sv:
    label = "contradiction"
else:
    label = "entailment"

print(label)
