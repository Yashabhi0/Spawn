from pathlib import Path

from devbootstrap.core.models import ProjectConfig
from devbootstrap.core.registry import get_template


class ProjectGenerator:
    def generate(self, config: ProjectConfig) -> None:
        template = get_template(config.template)

        if template is None:
            raise ValueError(f"Unknown template: {config.template}")

        project_path = Path(config.name)

        project_path.mkdir(exist_ok=True)

        for folder in template.folders:
            (project_path / folder).mkdir(exist_ok=True)

        print(f"Created project: {config.name}")
        print(f"Template: {template.name}")