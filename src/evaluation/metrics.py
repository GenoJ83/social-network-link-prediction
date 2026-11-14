"""Link prediction evaluation: ROC-AUC and Average Precision (AP)."""
from sklearn.metrics import roc_auc_score, average_precision_score
import numpy as np

def evaluate_link_predictions(pos_scores, neg_scores):
    y_true = np.concatenate([np.ones(len(pos_scores)), np.zeros(len(neg_scores))])
    y_scores = np.concatenate([pos_scores, neg_scores])
    roc = roc_auc_score(y_true, y_scores)
    ap = average_precision_score(y_true, y_scores)
    return {"roc_auc": round(float(roc), 4), "average_precision": round(float(ap), 4)}
