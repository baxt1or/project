FROM python:3.9-slim

WORKDIR /docker

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of your application
COPY . .

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
