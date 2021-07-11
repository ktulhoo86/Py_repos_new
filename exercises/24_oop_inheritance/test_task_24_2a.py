import pytest
import task_24_2a
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_2a, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_24_2a.MyNetmiko(**first_router_from_devices_yaml)
    r1.disconnect()
    assert isinstance(r1, CiscoIosSSH), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(r1, method="send_command")
    check_attr_or_method(r1, method="_check_error_in_command")


@pytest.mark.parametrize(
    "error,com_mand",
    [
        ("Invalid input detected", "sh ip br"),
        ("Incomplete com_mand", "logging"),
        ("Ambiguous com_mand", "a"),
    ],
)
def test_errors(first_router_from_devices_yaml, command, error):
    r1 = task_24_2a.MyNetmiko(**first_router_from_devices_yaml)
    with pytest.raises(task_24_2a.ErrorInCommand) as excinfo:
        return_value = r1.send_command(command)
        r1.disconnect()
    assert error in str(
        excinfo
    ), "Метод send_config_commands должен генерировать исключение, когда команда выполнена с ошибкой"
