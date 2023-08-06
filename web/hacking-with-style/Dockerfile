# Use the official Node.js 18.x image as base image
FROM node:18

# Install the latest version of Chrome dev package and fonts to support major charsets
# Note: This installs the necessary libs to make the bundled version of Chromium that Puppeteer installs work.
RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg \
    && sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-khmeros fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r pptruser && useradd -rm -g pptruser -G audio,video pptruser

# Set the user as "pptruser"
USER pptruser

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the image and install dependencies
COPY app/package*.json ./
RUN npm install

# Copy the rest of the application code to the image and build the app
COPY app ./
RUN npm run build

# Set the environment variable APP_ROOT to /app
ENV APP_ROOT=/app

# Expose port 8080
EXPOSE 8080

# Run "npm start" when the container starts
# Not sure why, but npm start invokes npm run build. caused permissions issues on CI-built images
CMD ["node", "dist/main.js"]
