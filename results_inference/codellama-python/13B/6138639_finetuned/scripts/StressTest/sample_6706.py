red_bricks_ratio_premise = 8
green_bricks_ratio_premise = 3
blue_bricks_ratio_premise = 1
red_bricks_ratio_hypothesis = 4
green_bricks_ratio_hypothesis = 3
blue_bricks_ratio_hypothesis = 1

# the hypothesis talks about the ratio of red, green, and blue bricks used to build a tower, referenced also in the premise
if red_bricks_ratio_hypothesis >= red_bricks_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than'red_bricks_ratio_premise'
    label = "contradiction"
elif green_bricks_ratio_hypothesis!= green_bricks_ratio_premise:
    # check if the green bricks ratio in the hypothesis contradicts the green bricks ratio reported in the premise
    label = "contradiction"
elif blue_bricks_ratio_hypothesis!= blue_bricks_ratio_premise:
    # check if the blue bricks ratio in the hypothesis contradicts the blue bricks ratio reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue bricks
    # any ratio less than'red_bricks_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
