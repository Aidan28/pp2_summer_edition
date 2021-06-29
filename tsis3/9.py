def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])