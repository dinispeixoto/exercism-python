import collections


def flatten(iterable):
    return [item for item in flatten_generator(iterable) if item is not None]


def flatten_generator(iterable):
    for item in iterable:
        if isinstance(item, collections.Iterable):
            yield from flatten(item)
        else:
            yield item
