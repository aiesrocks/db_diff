FROM ubuntu

ENV ACCEPT_EULA=Y 

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    python3 \
    python3-pip
#RUN pip install sqlalchemy pandas pyodbc
RUN apt-get install -y python3-sqlalchemy python3-pandas python3-pyodbc
RUN apt-get install -y git curl vim telnet docker.io
RUN apt-get install -y mariadb-client
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/ubuntu/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2)/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN curl -sSL -O https://packages.microsoft.com/config/ubuntu/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2)/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get install -y msodbcsql18 mssql-tools18 unixodbc-dev
RUN apt-get dist-clean
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> /etc/profile.d/mssql-tools.sh