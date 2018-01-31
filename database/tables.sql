
CREATE DATABASE home;

\c home;

-- Tables definitions

CREATE TABLE IF NOT EXISTS data (
  id SERIAL,
  hour              integer     not null,
  day               varchar     not null,
  tv_status         boolean     not null,
  screen_status     boolean     not null,
  light_1_status    boolean     not null,
  light_2_status    boolean     not null,
  light_1_intensity float       not null,
  light_2_intensity float       not null,
  light_1_color     float       not null,
  light_2_color     float       not null
);
