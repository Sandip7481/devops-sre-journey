#Every line in a Dockerfile creates a layer. Docker caches each layer.
FROM python:3.11-slim        
# Layer 1 — base OS + Python
WORKDIR /app 
# Layer 2 — set directory
COPY requirements.txt .
# Layer 3 — copy requirements FIRST
RUN pip install -r requirements.txt
# Layer 4 — install dependencies
COPY . .                     
# Layer 5 — copy your actual code
ENTRYPOINT ["python", "app.py"]
# Layer 6 — default command