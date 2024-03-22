FROM python:3.9

ARG SUPABASE_KEY=ey.c2JMTjoyMDI2NjU0ODcwfQ.6qzxwcFvS_yDDnjOogD-9U
ARG SUPABASE_URL=https://<projectid>.supabase.co
ARG ASSETS_PATH=/incest
ARG BUCKET_NAME=sample

ENV SUPABASE_KEY=${SUPABASE_KEY}
ENV SUPABASE_URL=${SUPABASE_URL}
ENV ASSETS_PATH=${ASSETS_PATH}
ENV BUCKET_NAME=${BUCKET_NAME}

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY scripts .

CMD [ "sleep", "360000" ]