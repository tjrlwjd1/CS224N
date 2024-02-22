# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

eval_path = "birth_dev.tsv"
eval = open(eval_path, "r")
len_eval = len(eval.readlines())
predicted_places = ["London"] * len_eval
total, correct = utils.evaluate_places(eval_path, predicted_places)
if total > 0:
    print(f"Correct: {correct} out of {total}: {correct/total*100}%")
else:
    print("No targets provided!")
