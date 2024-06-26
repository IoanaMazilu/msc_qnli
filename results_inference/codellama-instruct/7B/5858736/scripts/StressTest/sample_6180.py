# define variables for the marks obtained by David in each subject
english_mark_premise = 86
mathematics_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

# define variables for the marks obtained by David in each subject in the hypothesis
english_mark_hypothesis = 16
mathematics_mark_hypothesis = 85
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# calculate the average marks for David in each subject
english_average_premise = (english_mark_premise + mathematics_mark_premise + physics_mark_premise + chemistry_mark_premise + biology_mark_premise) / 5
english_average_hypothesis = (english_mark_hypothesis + mathematics_mark_hypothesis + physics_mark_hypothesis + chemistry_mark_hypothesis + biology_mark_hypothesis) / 5

# compare the average marks in each subject between the premise and the hypothesis
if english_average_premise <= english_average_hypothesis:
    # check if the estimate of 'english_average_hypothesis' contradicts the average marks in English reported in the premise
    label = "contradiction"
elif mathematics_average_hypothesis!= mathematics_average_premise:
    # check if the average marks in Mathematics in the hypothesis contradicts the average marks in Mathematics reported in the premise
    label = "contradiction"
elif physics_average_hypothesis!= physics_average_premise:
    # check if the average marks in Physics in the hypothesis contradicts the average marks in Physics reported in the premise
    label = "contradiction"
elif chemistry_average_hypothesis!= chemistry_average_premise:
    # check if the average marks in Chemistry in the hypothesis contradicts the average marks in Chemistry reported in the premise
    label = "contradiction"
elif biology_average_hypothesis!= biology_average_premise:
    # check if the average marks in Biology in the hypothesis contradicts the average marks in Biology reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
