-- SQL script to rank country origins by total number of fans
-- This script assumes the existence of a table named `metal_bands` with columns `origin` and `fans`.

SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
WHERE
    origin IS NOT NULL AND fans IS NOT NULL
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
