def  apply_all_func(int_inst, *functions):
    results = {}
    for f in functions:
        results[f.__name__] = f(int_inst)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))