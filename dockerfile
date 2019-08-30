#Use alpine (lightweight image basedon Alpine Linux
#Use multi-stage, name stage one as "base" as builder
FROM python:3 as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

RUN pip install scipy

# Second stage, detach requirements from app
FROM base

COPY --from=builder /install /usr/local
COPY src /app

# Make port 80 available to outside World
EXPOSE 80

WORKDIR /app
