FROM public.ecr.aws/lambda/python:3.8

COPY ["requirements.txt", "cifar10.script.pt", "index_to_name.json", "lambda_function.py", "utils.py", "./"]

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "lambda_function.lambda_handler" ]