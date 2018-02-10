import numpy as np
import pandas as pd

file_house = "..\\house_cate2avg.csv"
file_raion = "..\\raions_raw_pct_all.csv"
file_macro = "..\\macro.csv"
file_macro_pca = "..\\macro_pca_cor_20.csv"


def read_input():
    house = pd.read_csv(file_house)
    raions = pd.read_csv(file_raion)
    macro = pd.read_csv(file_macro)
    data = pd.merge(house, raions, on="sub_area")
    data = pd.merge(data, macro, on="timestamp")
    data.drop("sub_area", 1, inplace=True)
    train = data[data["test"] == 0]
    test = data[data["test"] == 1]
    train.drop("test", 1, inplace=True)
    trainy = train["price_doc"]
    train.drop("price_doc", 1, inplace=True)
    train.drop("id", 1, inplace=True)
    test.drop("test", 1, inplace=True)
    test.drop("price_doc", 1, inplace=True)
    test_id = test["id"]
    test.drop("id", 1, inplace=True)
    return train, trainy, test, test_id


def read_input_pca():
    house = pd.read_csv(file_house)
    raions = pd.read_csv(file_raion)
    macro = pd.read_csv(file_macro_pca)
    data = pd.merge(house, raions, on="sub_area")
    data = pd.merge(data, macro, on="timestamp")
    data.drop("sub_area", 1, inplace=True)
    train = data[data["test"] == 0]
    test = data[data["test"] == 1]
    train.drop("test", 1, inplace=True)
    trainy = train["price_doc"]
    train.drop("price_doc", 1, inplace=True)
    train.drop("id", 1, inplace=True)
    test.drop("test", 1, inplace=True)
    test.drop("price_doc", 1, inplace=True)
    test_id = test["id"]
    test.drop("id", 1, inplace=True)
    return train, trainy, test, test_id


def read_xy():
    house = pd.read_csv(file_house)
    raions = pd.read_csv(file_raion)
    macro = pd.read_csv(file_macro)
    data = pd.merge(house, raions, on="sub_area")
    data = pd.merge(data, macro, on="timestamp")
    train = data[data["test"] == 0]
    trainy = train["price_doc"]
    data.drop("price_doc", 1, inplace=True)
    data.drop("test", 1, inplace=True)
    return data, trainy


def read_train():
    house = pd.read_csv(file_house)
    raions = pd.read_csv(file_raion)
    macro = pd.read_csv(file_macro_pca)
    data = pd.merge(house, raions, on="sub_area")
    data = pd.merge(data, macro, on="timestamp")
    data = data[data["test"] == 0]
    data.drop("sub_area", 1, inplace=True)
    data.drop("test", 1, inplace=True)
    data.drop("id", 1, inplace=True)
    train = data[(np.array(data.index) % 5) != 0]
    test = data[(np.array(data.index) % 5) == 0]
    trainy = train['price_doc']
    testy = test['price_doc']
    train.drop("price_doc", 1, inplace=True)
    test.drop("price_doc", 1, inplace=True)
    return train, trainy, test, testy


def read_train_pca():
    house = pd.read_csv(file_house)
    raions = pd.read_csv(file_raion)
    macro = pd.read_csv(file_macro_pca)
    data = pd.merge(house, raions, on="sub_area")
    data = pd.merge(data, macro, on="timestamp")
    data = data[data["test"] == 0]
    data.drop("sub_area", 1, inplace=True)
    data.drop("test", 1, inplace=True)
    data.drop("id", 1, inplace=True)
    train = data[(np.array(data.index) % 5) != 0]
    test = data[(np.array(data.index) % 5) == 0]
    trainy = train['price_doc']
    testy = test['price_doc']
    train.drop("price_doc", 1, inplace=True)
    test.drop("price_doc", 1, inplace=True)
    return train, trainy, test, testy
