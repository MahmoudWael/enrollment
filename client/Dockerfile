FROM node:alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

# Copy the contents of the project to the image
COPY . .

# Run 'npm start' when the container starts.
CMD ["npm", "run", "start"]