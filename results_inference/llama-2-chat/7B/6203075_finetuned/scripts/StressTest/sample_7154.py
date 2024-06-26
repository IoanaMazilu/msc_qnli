# Read the premise and hypothesis
premise_pink = 9
premise_yellow = 8
premise_blue = 5
hypothesis_pink = 3
hypothesis_yellow = 8
hypothesis_blue = 5

# The hypothesis refers to the number of highlighters in the teacher's desk, which is also mentioned in the premise
# However, the hypothesis provides different numbers for each color of highlighter
if premise_pink!= hypothesis_pink:
    # If the number of pink highlighters in the hypothesis contradicts the number of pink highlighters in the premise,
    # then the hypothesis is contradictory to the premise
    label = "contradiction"
elif premise_yellow!= hypothesis_yellow:
    # If the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters in the premise,
    # then the hypothesis is contradictory to the premise
    label = "contradiction"
elif premise_blue!= hypothesis_blue:
    # If the number of blue highlighters in the hypothesis contradicts the number of blue highlighters in the premise,
    # then the hypothesis is contradictory to the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, then the label is neutral
    label = "neutral"

print(label)
