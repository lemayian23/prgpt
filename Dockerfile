FROM node:18
WORKDIR /app
COPY api/ ./api/
RUN cd api && npm install
CMD ["node", "api/app.py"]