FROM python:3.9-alpine
WORKDIR /app
RUN apk add --no-cache python3 py3-pip
RUN python3 --version
RUN pip3 --version
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
ENV PORT 8000
VOLUME /API/data
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "app:app"]
