FROM python:3

WORKDIR /app

# Copy the source code into the container.
COPY . .

#RUN pip install numpy
#RUN pip install pandas
#RUN pip install matplotlib
ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Run the application.
#CMD [ "python3", "test.py" ]
CMD [ "sh"]


