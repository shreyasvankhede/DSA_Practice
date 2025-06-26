"""
Problem: Combine Two Tables
LeetCode: https://leetcode.com/problems/combine-two-tables/
Category: SQL to Pandas (Join Operation)
"""

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(person, address, on="personId", how="left")
    merged = merged.drop(["personId", "addressId"], axis=1)
    merged = merged[['firstName', 'lastName', 'city', 'state']]
    return merged


if __name__ == "__main__":
    # Sample test case
    person_data = {
        "personId": [1, 2],
        "firstName": ["John", "Jane"],
        "lastName": ["Doe", "Smith"]
    }
    address_data = {
        "addressId": [1],
        "personId": [1],
        "city": ["New York"],
        "state": ["NY"]
    }

    person_df = pd.DataFrame(person_data)
    address_df = pd.DataFrame(address_data)

    result = combine_two_tables(person_df, address_df)
    print(result)

    # Expected output:
    #   firstName lastName      city state
    # 0      John      Doe  New York    NY
    # 1      Jane    Smith       NaN   NaN
