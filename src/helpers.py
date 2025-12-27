
# compouned annual growth rate
def cagr(start_value, end_value, years):
    return (end_value / start_value) ** (1 / years) - 1
