# Dockerfile for Spring Boot + Python ML Engine Deployment on Render
FROM eclipse-temurin:17-jdk-jammy AS build

# Install Maven
RUN apt-get update && apt-get install -y maven

WORKDIR /app
COPY backend ./backend
WORKDIR /app/backend
RUN mvn clean package -DskipTests

# Final stage: Java JRE + Python 3 ML Runtime
FROM eclipse-temurin:17-jre-jammy

# Install Python3, pip and ML libraries required for fraud detection model
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir pandas numpy scikit-learn joblib

WORKDIR /app

# Copy compiled Spring Boot JAR and ML Model files
COPY --from=build /app/backend/target/*.jar app.jar
COPY backend/mlmodel ./mlmodel

EXPOSE 8080

ENV PORT=8080
ENV PYTHON_PATH=python3

CMD ["sh", "-c", "java -Dserver.port=${PORT} -jar app.jar"]
