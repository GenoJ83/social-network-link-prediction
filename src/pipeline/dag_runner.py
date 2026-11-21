from typing import Dict, List, Callable, Any

class DagStageRunner:
    def __init__(self):
        self.stages: Dict[str, Callable[[Any], Any]] = {}
        self.order: List[str] = []

    def add_stage(self, name: str, fn: Callable[[Any], Any]) -> "DagStageRunner":
        self.stages[name] = fn
        self.order.append(name)
        return self

    def execute(self, initial_input: Any) -> Dict[str, Any]:
        data = initial_input
        outputs = {}
        for name in self.order:
            data = self.stages[name](data)
            outputs[name] = data
        return outputs
