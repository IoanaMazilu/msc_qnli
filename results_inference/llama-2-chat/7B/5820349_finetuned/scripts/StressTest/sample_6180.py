english_marks_premise = 86
mathematics_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 16
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or \
   mathematics_marks_premise <= mathematics_marks_hypothesis or \
   physics_marks_premise <= physics_marks_hypothesis or \
   chemistry_marks_premise <= chemistry_marks_hypothesis or \
   biology_marks_premise <= biology_marks_hypothesis:
    # check if the marks in any subject in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
elif english_marks_hypothesis > english_marks_premise and \
     mathematics_marks_hypothesis == mathematics_marks_premise and \
     physics_marks_hypothesis == physics_marks_premise and \
     chemistry_marks_hypothesis == chemistry_marks_premise and \
     biology_marks_hypothesis == biology_marks_premise:
    # check if the marks in any subject in the hypothesis is more than the marks reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
