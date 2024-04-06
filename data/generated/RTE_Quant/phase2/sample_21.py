# Premise: The 8,568-meter Mt. Kanchenjunga, the third highest in the world, is located in the border area of Nepal, India and China.
# Hypothesis: Kanchenjunga is 8586 meters high.
# Golden Label: neutral

mt_height_premise = 8568
mt_height_hypothesis = 8586

# the hypothesis talks about the height of Kanchenjunga which is also mentioned in the premise
if mt_height_hypothesis != mt_height_premise:
    # check if the height in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the height in the hypothesis does not contradict the height in the premise, we can infer entailment
    label = "entailment"

print(label)

