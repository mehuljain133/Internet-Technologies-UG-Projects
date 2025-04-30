# Configure a web-server on a personal system.

#!/bin/bash

# Step 1: Update and Upgrade System
echo "Updating and upgrading the system..."
sudo apt update -y
sudo apt upgrade -y

# Step 2: Install Apache Web Server
echo "Installing Apache web server..."
sudo apt install apache2 -y

# Step 3: Start Apache Web Server
echo "Starting Apache web server..."
sudo systemctl start apache2
sudo systemctl enable apache2

# Step 4: Check Apache Status
echo "Checking Apache status..."
sudo systemctl status apache2 | grep "Active"

# Step 5: Configure Apache Virtual Hosts (for multiple websites)
echo "Configuring Apache Virtual Hosts..."

# Create directories for website files
sudo mkdir -p /var/www/mywebsite/public_html

# Set permissions for the website directory
sudo chown -R $USER:$USER /var/www/mywebsite/public_html

# Create a sample index.html for the website
echo "<html><body><h1>Welcome to My Website</h1></body></html>" > /var/www/mywebsite/public_html/index.html

# Create a new Apache configuration file for the site
echo "
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/mywebsite/public_html
    ServerName mywebsite.local

    ErrorLog \${APACHE_LOG_DIR}/error.log
    CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>" | sudo tee /etc/apache2/sites-available/mywebsite.conf

# Enable the new site and reload Apache
sudo a2ensite mywebsite.conf
sudo systemctl reload apache2

# Step 6: Update the hosts file to point to localhost for the new domain
echo "127.0.0.1 mywebsite.local" | sudo tee -a /etc/hosts

# Step 7: Test Apache Setup
echo "Testing Apache setup..."
echo "Open your browser and go to http://mywebsite.local"
echo "You should see 'Welcome to My Website'"

# Step 8: Install NGINX Web Server (Optional)
echo "Installing NGINX web server..."
sudo apt install nginx -y

# Step 9: Start NGINX Web Server
echo "Starting NGINX web server..."
sudo systemctl start nginx
sudo systemctl enable nginx

# Step 10: Check NGINX Status
echo "Checking NGINX status..."
sudo systemctl status nginx | grep "Active"

# Step 11: Configure NGINX (Optional: Configure Virtual Hosts)
echo "Configuring NGINX Virtual Hosts..."

# Create directory for the NGINX website
sudo mkdir -p /var/www/nginxwebsite

# Set permissions for the NGINX directory
sudo chown -R $USER:$USER /var/www/nginxwebsite

# Create a sample index.html for NGINX
echo "<html><body><h1>Welcome to NGINX Website</h1></body></html>" > /var/www/nginxwebsite/index.html

# Create a new NGINX configuration file for the site
echo "
server {
    listen 80;
    server_name nginxwebsite.local;
    root /var/www/nginxwebsite;

    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}" | sudo tee /etc/nginx/sites-available/nginxwebsite

# Create symbolic link for NGINX site
sudo ln -s /etc/nginx/sites-available/nginxwebsite /etc/nginx/sites-enabled/

# Test NGINX configuration
sudo nginx -t

# Reload NGINX to apply changes
sudo systemctl reload nginx

# Step 12: Update the hosts file to point to localhost for NGINX
echo "127.0.0.1 nginxwebsite.local" | sudo tee -a /etc/hosts

# Step 13: Test NGINX Setup
echo "Testing NGINX setup..."
echo "Open your browser and go to http://nginxwebsite.local"
echo "You should see 'Welcome to NGINX Website'"

# Step 14: Enable Firewall (Optional) for Apache & NGINX
echo "Allowing HTTP traffic through the firewall..."

# Allow Apache and NGINX traffic through the firewall
sudo ufw allow 'Apache Full'
sudo ufw allow 'Nginx Full'

# Enable firewall (if not already enabled)
sudo ufw enable

# Step 15: Clean up and final check
echo "Cleaning up..."
sudo apt autoremove -y

echo "Web server setup completed successfully!"
echo "-----------------------------------------------------"
echo "You have set up Apache on 'mywebsite.local' and NGINX on 'nginxwebsite.local'."
echo "Make sure to test the servers by opening the websites in your browser."

# End of script
