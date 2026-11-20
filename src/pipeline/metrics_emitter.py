from typing import Dict, Any

class PipelineMetricsEmitter:
    @staticmethod
    def format_prometheus_metrics(stage_times: Dict[str, float]) -> str:
        lines = []
        for stage, duration in stage_times.items():
            lines.append(f'pipeline_stage_duration_seconds{{stage="{stage}"}} {round(duration, 4)}')
        return "\n".join(lines)
