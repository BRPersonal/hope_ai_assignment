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
    children = int(input("Enter no. of children:"))
    sex_male = True if input("Is Male(y/n)?:").lower() == "y" else False
    smoker_yes = True if input("Is smoker(y/n)?:").lower() == "y" else False
    samples.append([age,bmi,children,sex_male,smoker_yes])

result = loaded_model.predict(samples)

print("---------Insurance Predictions------------")
for i in range(no_of_inputs):
  print(f"""
          age={samples[i][0]}, 
          bmi={samples[i][1]}, 
          children={samples[i][2]},
          gender={"male" if samples[i][3] else "female"},
          smoker={"yes" if samples[i][4] else "no"},
          predictedInsurance={result[i]:.2f}
         """
        )
