calories_per_candy_premise = 3.0
total_calories_hypothesis = 18.0
candy_bars_hypothesis = 5.0

# the hypothesis refers to the total calories in candy bars, which can be calculated from the premise
# compute the total calories from the premise
total_calories_premise = calories_per_candy_premise * candy_bars_hypothesis
if total_calories_hypothesis != total_calories_premise:
    # check if the total calories in the hypothesis contradicts the calculated total calories from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
