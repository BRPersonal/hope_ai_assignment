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
    
    return best_combo
