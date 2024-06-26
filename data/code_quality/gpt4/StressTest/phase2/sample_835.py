english_mark_premise = 66
english_mark_hypothesis = 76
math_mark_premise = 65
math_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# The hypothesis refers to the marks obtained by David in different subjects, which are also mentioned in the premise
if english_mark_hypothesis <= english_mark_premise or math_mark_hypothesis <= math_mark_premise or physics_mark_hypothesis <= physics_mark_premise or chemistry_mark_hypothesis <= chemistry_mark_premise or biology_mark_hypothesis <= biology_mark_premise:
    # Check if the hypothesis contradicts the premise by stating that David obtained less or equal marks than mentioned in the premise
    label = "contradiction"
elif english_mark_hypothesis > english_mark_premise and math_mark_hypothesis == math_mark_premise and physics_mark_hypothesis == physics_mark_premise and chemistry_mark_hypothesis == chemistry_mark_premise and biology_mark_hypothesis == biology_mark_premise:
    # If the hypothesis values do not contradict the premise and David obtained more marks in English than mentioned in premise, it can be inferred as entailment
    label = "entailment"
else:
    # If the hypothesis values do not contradict the premise and cannot be fully and explicitly entailed from the premise either, it is neutral
    label = "neutral"

print(label)
