import pytest

from camel.prompts import PromptTemplate
from camel.typing import RoleType, TaskType


@pytest.mark.parametrize('task_role_tuple', [
    (TaskType.AI_SOCIETY, RoleType.ASSISTANT),
    (TaskType.AI_SOCIETY, RoleType.USER),
    (TaskType.CODE, RoleType.ASSISTANT),
    (TaskType.CODE, RoleType.USER),
    (TaskType.MISALIGNMENT, RoleType.ASSISTANT),
    (TaskType.MISALIGNMENT, RoleType.USER),
    (TaskType.TRANSLATION, RoleType.ASSISTANT),
])
def test_get_system_prompt(task_role_tuple):
    task_type, role_type = task_role_tuple
    prompt_template = PromptTemplate.get_system_prompt(task_type, role_type)
    assert isinstance(prompt_template, PromptTemplate)


@pytest.mark.parametrize(
    'task_type', [TaskType.AI_SOCIETY, TaskType.CODE, TaskType.MISALIGNMENT])
def test_get_generate_tasks_prompt(task_type):
    prompt_template = PromptTemplate.get_generate_tasks_prompt(task_type)
    assert isinstance(prompt_template, PromptTemplate)


@pytest.mark.parametrize(
    'task_type', [TaskType.AI_SOCIETY, TaskType.CODE, TaskType.MISALIGNMENT])
def test_get_task_specify_prompt(task_type):
    prompt_template = PromptTemplate.get_task_specify_prompt(task_type)
    assert isinstance(prompt_template, PromptTemplate)