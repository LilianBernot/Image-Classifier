from datetime import datetime, timedelta
import random

def generate_random_dates() -> list[datetime]:

    # Generate a mix of dense and sparse dates
    dense_start = datetime(2023, 1, 1)
    sparse_start = datetime(2023, 2, 1)

    # Dense period: Many dates close together
    dense_dates = [dense_start + timedelta(days=random.randint(0, 5)) for _ in range(20)]

    # Sparse period: Dates further apart
    sparse_dates = [sparse_start + timedelta(days=random.randint(7, 20)) for _ in range(10)]

    # Another dense period
    second_dense_start = datetime(2023, 3, 15)
    second_dense_dates = [second_dense_start + timedelta(days=random.randint(0, 3)) for _ in range(15)]

    # Combine and shuffle the dates
    all_dates = dense_dates + sparse_dates + second_dense_dates

    return sorted(all_dates)