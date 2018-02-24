#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter

name, age, tech, skill = range(0, 4)

data = [
    ['alice', 24, 'blue', 86],
    ['alice', 24, 'green', 80],
    ['bob', 20, 'red', 76],
    ['bob', 20, 'green', 68],
    ['charlie', 45, 'blue', 96],
    ['dylan', 32, 'blue', 75],
    ['dylan', 32, 'green', 81],
    ['dylan', 32, 'red', 54],
    ['evelyn', 29, 'green', 83],
    ['evelyn', 29, 'red', 78],
    ['francis', 19, 'red', 64]
]


def get_answer_imperative(_data):
    answer = {}

    for row in _data:
        if row[age] >= 40:
            continue

        if row[tech] in answer:
            answer[row[tech]] = max(answer[row[tech]], (row[skill], row[name]))
        else:
            answer[row[tech]] = (row[skill], row[name])

    return {_tech: skill_name[1] for (_tech, skill_name) in answer.items()}


def get_programmers_two_skills_gt_75(_data):
    return [
        n for n, rows in
        dict(
            map(
                lambda (_name, rows): (_name, list(rows)),
                groupby(
                    sorted(
                        filter(
                            lambda row: row[skill] > 75,
                            _data
                        ),
                        key=itemgetter(name)
                    ),
                    lambda groups: groups[name]
                )
            )
        ).iteritems()
        if len(rows) >= 2
    ]


def get_answer_functional(_data):
    return dict(
        map(
            lambda (_tech, rows): (_tech, max(rows, key=itemgetter(skill))[name]),
            groupby(
                sorted(
                    filter(
                        lambda row: row[age] < 40,
                        _data
                    ),
                    key=itemgetter(tech)
                ),
                lambda groups: groups[tech]
            )
        )
    )

if __name__ == '__main__':
    print('Imperative Answer: {0}'.format(get_answer_imperative(data)))
    print('Functional Answer: {0}'.format(get_answer_functional(data)))

    print('Functional Answer 2: {0}'.format(get_programmers_two_skills_gt_75(data)))
    res = get_programmers_two_skills_gt_75(data)
    import simplejson as simplejson; print 'res: {json}'.format(json=simplejson.dumps(res, indent=4))