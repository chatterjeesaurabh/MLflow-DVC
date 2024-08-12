import mlflow

def calculator(a, b, operation):
    if operation=='add':
        return (a+b)
    if operation=='sub':
        return (a-b)
    if operation=='mul':
        return (a*b)
    if operation=='div':
        return (a/b)
    
    


if __name__=='__main__':
    a, b = 6, 5
    operation = 'sub'

    with mlflow.start_run():                            # start MLflow server
        mlflow.log_param('a', a)                        # add Parameters
        mlflow.log_param('b', b)
        mlflow.log_param('operation', operation)

        result = calculator(a, b, operation)
        mlflow.log_param('result', result) 

        print(f"Result: {operation} is {result}")



# stores params / artifacts / metrics data for each run in : 'mlruns' folder

# MLflow Interface command: 'mlflow ui' : click on the URL (e.g http://127.0.0.1:5000)


