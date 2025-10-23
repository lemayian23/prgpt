FROM python:3.12-slim
WORKDIR /app
# Install API dependencies first for better layer caching
COPY api/requirements.txt api/requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt
# Copy API source
COPY api/ ./api/
EXPOSE 3000
CMD ["python", "api/app.py"]