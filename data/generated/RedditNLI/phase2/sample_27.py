# Premise: Marijuana Re-crim Protest With Senator Scott Brown Video Part 2, Supporter Tries To School Marijuana Policy Expert, MA GOP Ferrari.
# Hypothesis: Marijuana Re-crim Protest With Senator Scott Brown Video Part 1; Senator Brushes Off Marijuana Reformers and Press.
# Golden Label: neutral

video_part_premise = 2
video_part_hypothesis = 1

# the hypothesis and premise mention different parts of a video series
if video_part_premise != video_part_hypothesis:
    # check if the part number in the hypothesis contradicts the part number in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise refer to the same part of the video series, we can infer entailment
    label = "entailment"

print(label)

