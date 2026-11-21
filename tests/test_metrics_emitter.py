from src.pipeline.metrics_emitter import PipelineMetricsEmitter

def test_metrics_emitter():
    prom = PipelineMetricsEmitter.format_prometheus_metrics({"clean": 0.005, "infer": 0.012})
    assert 'stage="clean"} 0.005' in prom
    assert 'stage="infer"} 0.012' in prom
