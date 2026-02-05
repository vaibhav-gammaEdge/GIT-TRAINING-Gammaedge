FROM python:3.13
WORKDIR /GIT-TRAINING-Gammaedge


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000


CMD ["uvicorn", "docker:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

