#!/usr/bin/env python


# Complete the function below.


def  OutputCommonManager( count):
    first_employee_name = raw_input()
    second_employee_name = raw_input()

    boss_name, employee_name = raw_input().split(' ')

    employees = []
    employees.append(
        {
            'name': employee_name,
            'parent': {
                'name': boss_name
            }
        }
    )

    for i in range(count - 2):
        manager_name, employee_name = raw_input().split(' ')

        employee = _find(employees, employee_name)
        if employee is None:
            employee = {
                'name': employee_name
            }
            employees.append(employee)

        manager = _find(employees, manager_name)
        if manager is None:
            manager = {
                'name': manager_name
            }
            employees.append(manager)

        employee['parent'] = manager

    first_employee = _find(employees, first_employee_name)
    second_employee = _find(employees, second_employee_name)

    parents_first = _parents(first_employee)
    parents_second = _parents(second_employee)

    res = None
    for parent in parents_first:
        if parent['name'] in [p['name'] for p in parents_second]:
            res = parent['name']
            break

    print res


def _find(nodes, name):
    res = [n for n in nodes if n['name'] == name]
    return res[0] if len(res) > 0 else None


def _parents(node):
    parents = []

    if 'parent' in node:
        parents.append(node['parent'])
        parents.extend(_parents(node['parent']))

    return parents


_count = int(raw_input());

OutputCommonManager(_count);