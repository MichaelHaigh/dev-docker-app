FROM centos:centos7.6.1810

LABEL maintainer="michael@nutanix.com"

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y update && \
    yum -y install git vim wget gcc libpqxx-devel python-pip python-devel postgresql-server postgresql-devel postgresql-contrib

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
