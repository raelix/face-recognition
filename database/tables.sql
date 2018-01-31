
CREATE DATABASE home;

\c home;

-- Tables definitions

CREATE TABLE IF NOT EXISTS data (
  id SERIAL,
  hour               integer       not null,
  day                varchar       not null,
  is_user_at_home    boolean       not null,
  n_of_people        integer       not null,
  tv_status          boolean       not null,
  light_1_status     boolean       not null,
  light_2_status     boolean       not null,
  light_1_color      varchar       not null,
  light_2_color      varchar       not null
);
