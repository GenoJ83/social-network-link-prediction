from src.pipeline.dag_runner import DagStageRunner

def test_dag_runner():
    dag = DagStageRunner()
    dag.add_stage("clean", lambda s: s.strip().lower())
    dag.add_stage("tokenize", lambda s: s.split())
    dag.add_stage("count", lambda tokens: len(tokens))
    outputs = dag.execute("  Hello World Test  ")
    assert outputs["clean"] == "hello world test"
    assert outputs["count"] == 3
