red_bricks_ratio = 4/1
green_bricks_ratio = 3/1
blue_bricks_ratio = 1/1

# the hypothesis talks about the ratio of red, green and blue bricks in the tower
if red_bricks_ratio <= 3 and green_bricks_ratio <= 3 and blue_bricks_ratio <= 3:
    label = "neutral"
elif red_bricks_ratio > 3 and green_bricks_ratio > 3 and blue_bricks_ratio > 3:
    label = "contradiction"
else:
    label = "entailment"

print(label)
