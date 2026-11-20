from src.explainability.permutation_importance import PermutationImportance

def test_permutation_importance():
    # score function rewards feature 0 heavily
    def score_fn(matrix):
        return sum(row[0] * 2.0 + row[1] * 0.1 for row in matrix)

    data = [[10.0, 1.0], [20.0, 2.0], [30.0, 3.0]]
    imp = PermutationImportance.calculate(score_fn, data, ["feat_important", "feat_noise"])
    assert "feat_important" in imp
    assert "feat_noise" in imp
