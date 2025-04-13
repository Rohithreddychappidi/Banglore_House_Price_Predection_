import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None
def Get_estimated_price(location,sqft,bhk,bath):
    try:

        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x=np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)
def Get_Location_Names():

    return __locations
def load_saved_route():
    print("loading")
    global __data_columns
    global __locations

    with open("./route/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open("./route/banglore_home_prices_model.pickle",'rb') as f:
                  __model = pickle.load(f)


if __name__ == "__main__":
    load_saved_route()
    print(Get_Location_Names())
    print(Get_estimated_price('2nd phase judicial layout',1000,3,2))