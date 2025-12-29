
from itertools import product
from sklearn.metrics import r2_score


def center_text(text:str,column_width:int) -> str:

    result = text
    length = len(text)

    if (column_width > length):
        filler_length = (column_width - length) // 2  #integer division
        filler_spaces = (" " * filler_length)
        result = filler_spaces + text + filler_spaces

    return result

"""
  zip() takes two or more iterables and returns a zip object (an iterator) of tuples
  stops when the shortest iterable is exhausted
  eg.,
  result = zip([1, 2, 3], ['a', 'b', 'c','d'])
  list_result = list(result)
  print(list_result)  # [(1, 'a'), (2, 'b'), (3, 'c')]
  similarly dict() will convert the result of zip() into dictionary

  product() from itertools takes two or more
  iterables and returns a list of tuples

  dict.values() returns a list of list in this case
  which has to be unpacked before sending it to product()
  That's what * does
  eg.,
  param_dict = {
    'n_estimators': [10, 50], 
    'max_depth': [3, 5]
  }
  param_dict.values() gives you: [[10, 50], [3, 5]]
  *param_dict.values() unpacks it to: [10, 50], [3, 5]
  product(*param_dict.values()) becomes: product([10, 50], [3, 5])
  This generates list of all combinations: [(10, 3), (10, 5), (50, 3), (50, 5)]
"""
def generate_parameter_combinations(param_dict:dict) -> [dict] :
    return [dict(zip(param_dict.keys(),combo)) for combo in product(*param_dict.values())]

def find_best_hyperparameters(param_dict, x_train, y_train, x_test, y_test, 
                            create_regressor_callback, print_combo_callback)-> dict:
    """
    Find the best hyperparameter combination using callbacks.
    
    Args:
        param_dict: Dictionary of various combinations of parameter values to try
        x_train, y_train: Training data
        x_test, y_test: Test data
        create_regressor_callback: Lambda that takes combo dict and returns a regressor
        print_combo_callback: Lambda that takes combo dict and prints it
    
    Returns:
        best_combo: Dictionary containing the best parameter combination with r_score
    """
    
    combinations = generate_parameter_combinations(param_dict)
    
    best_combo = None
    max_r_score = float('-inf')
    
    for combo in combinations:
        regressor = create_regressor_callback(combo)
        regressor.fit(x_train, y_train)
        y_predict = regressor.predict(x_test)
        r_score = r2_score(y_test, y_predict)
        combo["r_score"] = r_score
        
        print_combo_callback(combo)
        
        if r_score > max_r_score:
            max_r_score = r_score
            best_combo = combo.copy()
            best_combo["regressor"] = regressor
    
    return best_combo
