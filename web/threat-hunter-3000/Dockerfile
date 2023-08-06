FROM node:16-alpine

# Copy and download dependencies
WORKDIR /web
COPY package*.json ./
RUN npm install

# Copy the source files into the image
COPY . .

RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "preview"]