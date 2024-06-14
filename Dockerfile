FROM python:3.9-alpine
WORKDIR /app
RUN apk add python3 py3-pip
RUN python3 --version
RUN pip3 --version
COPY Persistence/ ./Persistence
COPY Model/ ./Model
COPY API/ ./API
COPY Tests/ ./Tests
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENV PORT 8000
VOLUME /app/Data
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
