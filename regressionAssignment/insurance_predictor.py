import pickle
import warnings 

#suppress warnings
warnings.filterwarnings('ignore')

finalized_model = "insurance_model.sav"
loaded_model = pickle.load(open(finalized_model,"rb"))

#Predict the output for multiple inputs
samples=[]
no_of_inputs = int(input("Enter no. of inputs:"))
for i in range(no_of_inputs):
    print(f"(Input #{i+1})\n----------------\n")
    age = int(input(f"Enter age:"))
    bmi = float(input("Enter Bmi:"))
    children = int(input("Enter no>of children:"))
    sex_male = bool(input("Is Male?:"))
    smoker_yes = bool(input("Is smoker?:"))
    samples.append([age,bmi,children,sex_male,smoker_yes])

result = loaded_model.predict(samples)
print(f"result.shape={result.shape}")
print(f"Predicted Insurance={result}")