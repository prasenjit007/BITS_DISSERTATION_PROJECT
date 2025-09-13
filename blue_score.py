import sacrebleu
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import precision_recall_fscore_support

# Define test cases
test_cases = [
    {
        "task": "Translation",
        "reference": "Bonjour, comment allez-vous aujourd'hui ?",
        "hypothesis": "Bonjour, comment ça va aujourd'hui ?"
    },
    {
        "task": "Summarization",
        "reference": "The cat sat on the mat and watched the dog.",
        "hypothesis": "The cat watched the dog from the mat."
    },
    {
        "task": "Paraphrasing",
        "reference": "She enjoys playing tennis during the weekend.",
        "hypothesis": "On weekends, she likes to play tennis."
    },
    {
        "task": "Translation",
        "reference": "Je suis allé au marché pour acheter des légumes.",
        "hypothesis": "Je suis allé au supermarché pour acheter des légumes."
    },
    {
        "task": "Summarization",
        "reference": "The report highlights the quarterly financial results showing a 20% increase in revenue.",
        "hypothesis": "The report shows a 20% revenue growth this quarter."
    }
]

# Evaluate scores
task_names = []
bleu_scores = []
f1_scores = []

for case in test_cases:
    reference = [case["reference"]]
    hypothesis = [case["hypothesis"]]

    # BLEU score
    bleu_result = sacrebleu.corpus_bleu([hypothesis[0]], [reference])
    bleu_scores.append(bleu_result.score)

    # F1 score (word-level binary vector)
    ref_words = set(reference[0].split())
    hyp_words = set(hypothesis[0].split())
    all_words = list(ref_words.union(hyp_words))

    y_true = [1 if word in ref_words else 0 for word in all_words]
    y_pred = [1 if word in hyp_words else 0 for word in all_words]

    _, _, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='binary')
    f1_scores.append(f1 * 100)

    task_names.append(case["task"])

# Create DataFrame
df = pd.DataFrame({
    "Task": task_names,
    "BLEU Score": bleu_scores,
    "F1 Score": f1_scores
})

# Reshape for grouped bar plot
df_melted = pd.melt(df, id_vars=["Task"], var_name="Metric", value_name="Score")

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="Task", y="Score", hue="Metric", data=df_melted)
plt.title("BLEU vs F1 Scores by Task Type")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
