premise_distance = 40
premise_maxwell_speed = 4
premise_brad_speed = 6

hypothesis_distance = 80
hypothesis_maxwell_speed = 4
hypothesis_brad_speed = 6

# calculate the distance traveled by Brad in the premise
premise_brad_distance = premise_distance / (premise_maxwell_speed + premise_brad_speed)

# calculate the distance traveled by Brad in the hypothesis
hypothesis_brad_distance = hypothesis_distance / (hypothesis_maxwell_speed + hypothesis_brad_speed)

# compare the distances traveled by Brad in the premise and hypothesis
if premise_brad_distance == hypothesis_brad_distance:
    label = "entailment"
elif premise_brad_distance!= hypothesis_brad_distance:
    label = "contradiction"
else:
    label = "neutral"

print(label)
