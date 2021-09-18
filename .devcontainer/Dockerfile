FROM python:3.8.3
WORKDIR /usr/app
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHON_VERSION=3.8 \
  PYTHONPATH=/workspaces/portfolio-manager \
  PATH=/home/python/.local/lib/python3.8/site-packages:/usr/local/bin:/home/python:/home/python/app/bin:$PATH:/usr/app:/root/.poetry/bin
RUN pip install -U pip
RUN pip install -U pytest
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version 1.1.8
RUN poetry config virtualenvs.create false
COPY pyproject.toml pyproject.toml
RUN poetry install
EXPOSE 9000
CMD ["ash"]