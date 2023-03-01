CREATE TABLE access_log (
  id INT NOT NULL AUTO_INCREMENT,
  date DATETIME NOT NULL,
  client_ip VARCHAR(255) NOT NULL,
  server_ip VARCHAR(255) NOT NULL,
  count INT DEFAULT 0,
  PRIMARY KEY (id)
);