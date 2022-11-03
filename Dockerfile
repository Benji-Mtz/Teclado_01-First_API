# FROM baseImage
FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask

# COPY mi_dir container -> / /app -> . .
COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0" ]

# docker build -t rest-apis-flask-python .
# docker run -d -p 5005:5000 rest-apis-flask-python