premise_pink_highlighters = 9
premise_yellow_highlighters = 8
premise_blue_highlighters = 5

hypothesis_pink_highlighters = 3
hypothesis_yellow_highlighters = 8
hypothesis_blue_highlighters = 5

# the hypothesis refers to the number of highlighters in Kaya's teacher's desk
if hypothesis_pink_highlighters <= premise_pink_highlighters and hypothesis_yellow_highlighters <= premise_yellow_highlighters and hypothesis_blue_highlighters <= premise_blue_highlighters:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives an estimate for the number of highlighters in Kaya's teacher's desk
    # any number of highlighters greater than or equal to the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
