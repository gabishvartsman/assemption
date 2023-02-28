CREATE TABLE access_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    client_ip VARCHAR(255),
    server_ip VARCHAR(255)
);

