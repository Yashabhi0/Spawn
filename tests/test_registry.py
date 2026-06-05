from spawn.core.registry import get_template


def test_python_template_exists():
    template = get_template("python")

    assert template is not None
    assert template.name == "Python Script"