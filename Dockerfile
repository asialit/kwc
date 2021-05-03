FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update && apt install -y gcc clang clang-tools cmake python3 python3-pip cppcheck valgrind git patchelf m4 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Install required Python libraries
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Clone and install HElib
RUN git clone https://github.com/homenc/HElib.git
WORKDIR /app/HElib
RUN mkdir build
WORKDIR /app/HElib/build
RUN cmake -DPACKAGE_BUILD=ON ..
RUN make -j16
RUN make install

WORKDIR /app
COPY . .

# build the C++ code
RUN cmake .
RUN make

# Run code
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
