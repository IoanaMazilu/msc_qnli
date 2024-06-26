# Define variables for the sides of the triangle
sides_st = 10
sides_tv = 10
sides_sv = 12

# Define variables for the sides of the hypothesis
hypothesis_st = 70
hypothesis_tv = 70
hypothesis_sv = 12

# Check if the sides of the hypothesis contradict the sides of the premise
if hypothesis_st!= sides_st or hypothesis_tv!= sides_tv or hypothesis_sv!= sides_sv:
    label = "contradiction"
else:
    label = "neutral"

print(label)
