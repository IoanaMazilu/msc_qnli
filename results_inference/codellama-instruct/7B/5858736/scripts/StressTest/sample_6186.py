blue_paint_premise = 16
fuchsia_premise = 86
mauve_paint_hypothesis = 10

if blue_paint_premise <= mauve_paint_hypothesis:
    label = "contradiction"
elif fuchsia_premise <= mauve_paint_hypothesis:
    label = "entailment"
else:
    label = "neutral"

print(label)
