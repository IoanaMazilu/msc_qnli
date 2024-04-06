# Premise: Phil Mickelson finished a triumphant week in his second home, winning the FBR Open by five strokes for his largest margin of victory in a PGA Tour event.
# Hypothesis: Mickelson won by five shots last week, the largest margin of his career.
# Golden Label: neutral

winning_margin_premise = 5
winning_margin_hypothesis = 5

largest_margin_premise = True 
largest_margin_hypothesis = True 

# the hypothesis talks about the margin of victory and whether it's the largest in his career
# both of these facts are presented in the premise
if winning_margin_hypothesis != winning_margin_premise:
    # check if the winning margin in the hypothesis contradicts the winning margin in the premise
    label = "contradiction"
elif largest_margin_hypothesis != largest_margin_premise:
    # check if the statement about this being the largest margin of his career contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

