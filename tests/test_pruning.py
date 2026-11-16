from src.quantization.pruning import MagnitudePruner

def test_pruning():
    weights = [0.1, 0.9, -0.05, 0.8, -0.7]
    mask = MagnitudePruner.compute_mask(weights, target_sparsity=0.4)
    pruned = MagnitudePruner.prune_weights(weights, mask)
    assert len(pruned) == 5
    assert pruned.count(0.0) >= 2
