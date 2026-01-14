# Stage 1: Build the React application
FROM node:18-alpine AS build
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the code and build
COPY . .
# Set Environment Variables for the build process
ARG REACT_APP_LINK_SERVICE_URL
ARG REACT_APP_ANALYTICS_SERVICE_URL
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine
# Copy build files from Stage 1 to Nginx public folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
