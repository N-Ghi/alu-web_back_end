-- SQL script to rank country origins by total number of fans
-- This script assumes the existence of a table named `metal_bands` with columns `origin` and `fans`.

SELECT origin, SUM(fans) AS nb_fans from metal_bands group by origin order by nb_fans DESC;