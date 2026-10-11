"""Helpers for writing Wealthwolf unit JSON. Steps get ids from their lesson
(<lessonId>-q1, -q2…) and every document asserts its own arithmetic."""
import json, os
from decimal import Decimal as D

DATA = '/Users/jackdworkin/Claude Code Projects/wealthwolf/src/data'
SECTION = 'everyday-money'


def money(x):
    return float(D(str(x)).quantize(D('0.01')))


def total(amounts):
    return money(sum(D(str(a)) for a in amounts))


def _step(kind, **fields):
    s = {'type': kind}
    for key in ('context', 'doc', 'docs'):
        if fields.get(key) is not None:
            s[key] = fields.pop(key)
        else:
            fields.pop(key, None)
    for k, v in fields.items():
        if v is not None:
            s[k] = v
    return s


def info(title, body, callout=None):
    return _step('info', title=title, body=body, callout=callout)


def mc(prompt, choices, answer, explain, context=None, doc=None, docs=None, why=None):
    assert 0 <= answer < len(choices)
    if why: assert len(why) == len(choices)
    return _step('multiple_choice', context=context, doc=doc, docs=docs, prompt=prompt, choices=choices,
                 answer=answer, why=why, explain=explain)


def tf(prompt, answer, explain, context=None, doc=None):
    assert isinstance(answer, bool)
    return _step('true_false', context=context, doc=doc, prompt=prompt, answer=answer, explain=explain)


def fill(prompt, choices, answer, explain, context=None):
    assert prompt.count('___') == 1
    return _step('fill_blank', context=context, prompt=prompt, choices=choices, answer=answer, explain=explain)


def num(prompt, answer, explain, context=None, doc=None, docs=None, unit='$', cents=None):
    s = _step('number', context=context, doc=doc, docs=docs, prompt=prompt, answer=answer, unit=unit)
    if cents or (cents is None and isinstance(answer, float) and answer != int(answer)):
        s['tolerance'] = 0.005
    s['explain'] = explain
    return s


def order(prompt, items, explain, context=None):
    assert len(items) >= 3 and len(set(items)) == len(items)
    return _step('order', context=context, prompt=prompt, items=items, explain=explain)


def match(prompt, pairs, explain=None, context=None):
    assert len(pairs) >= 3 and len({p[1] for p in pairs}) == len(pairs)
    return _step('match', context=context, prompt=prompt, pairs=[list(p) for p in pairs], explain=explain)


def sort(prompt, buckets, items, explain=None, context=None):
    assert len(buckets) >= 2 and len(items) >= 3 and all(0 <= b < len(buckets) for _, b in items)
    return _step('sort', context=context, prompt=prompt, buckets=buckets, items=[list(i) for i in items], explain=explain)


def spot(prompt, doc, answer, explain, context=None):
    assert any(l['id'] == answer for l in doc['lines']), answer
    return _step('spot', context=context, prompt=prompt, doc=doc, answer=answer, explain=explain)


def alloc(prompt, total_, step, categories, explain, context=None):
    return _step('allocate', context=context, prompt=prompt, total=total_, step=step, categories=categories, explain=explain)


def doc(kind, title, lines, subtitle=None, meta=None, totals=None, note=None):
    """lines: (id, label, amount) or (id, label, amount, {date/qty/section})."""
    out = []
    for line in lines:
        lid, label, amount = line[:3]
        entry = {'id': lid}
        extra = line[3] if len(line) > 3 else {}
        if 'section' in extra: entry['section'] = extra['section']
        if 'date' in extra: entry['date'] = extra['date']
        entry['label'] = label
        if 'qty' in extra: entry['qty'] = extra['qty']
        entry['amount'] = money(amount)
        out.append(entry)
    assert len({l['id'] for l in out}) == len(out)
    d = {'kind': kind, 'title': title}
    if subtitle: d['subtitle'] = subtitle
    if meta: d['meta'] = meta
    d['lines'] = out
    if totals: d['totals'] = [{'label': t[0], 'amount': money(t[1]), **({'strong': True} if len(t) > 2 and t[2] else {})} for t in totals]
    if note: d['note'] = note
    return d


def lesson(lid, title, summary, steps, fmt=None, story=None, xp=10):
    l = {'id': lid, 'type': 'lesson'}
    if fmt and fmt != 'concept': l['format'] = fmt
    l.update({'title': title, 'summary': summary, 'xp': xp})
    if story: l['story'] = story
    l['steps'] = [{'id': f'{lid}-q{i + 1}', **s} for i, s in enumerate(steps)]
    assert len(l['steps']) >= 5, lid
    return l


def review(prefix):
    return {'id': f'{prefix}-review', 'type': 'review', 'title': 'Sharpen Up',
            'summary': 'Smart repetition on what you’re closest to forgetting.', 'xp': 10, 'draw': 8, 'steps': []}


def trial(prefix, title, steps, draw=4):
    lid = f'{prefix}-trial'
    return {'id': lid, 'type': 'boss', 'title': f'Den Trial: {title}',
            'summary': f'{len(steps) + draw} questions. Three strikes and you’re out.', 'xp': 25, 'draw': draw,
            'steps': [{'id': f'{lid}-q{i + 1}', **s} for i, s in enumerate(steps)]}


def write_unit(filename, uid, order_, title, description, wolf, terms, lessons, section=None):
    section = section or SECTION
    ids = [l['id'] for l in lessons]
    assert len(set(ids)) == len(ids)
    unit = {'id': uid, 'section': section, 'order': order_, 'title': title, 'description': description,
            'wolfLine': wolf, 'terms': terms, 'lessons': lessons}
    path = os.path.join(DATA, section, filename)
    with open(path, 'w') as f:
        json.dump(unit, f, indent=2, ensure_ascii=False)
        f.write('\n')
    n = sum(len(l['steps']) for l in lessons)
    print(f'{filename}: {len([l for l in lessons if l["type"] == "lesson"])} lessons, {n} steps, {len(terms)} terms')


def term(name, definition, example=None):
    t = {'term': name, 'definition': definition}
    if example: t['example'] = example
    return t
