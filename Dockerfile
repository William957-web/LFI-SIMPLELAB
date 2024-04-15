FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask==2.3.1
RUN pip3 install Flask-Markdown
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
