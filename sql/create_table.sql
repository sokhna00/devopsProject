CREATE TABLE IF NOT EXISTS management_customuser (
  username varchar(450) NOT NULL,
  email varchar(450) NOT NULL,
  first_name varchar(450) NOT NULL,
  last_name varchar(450) NOT NULL,
  PRIMARY KEY (username)
);