-- SQL script to rank country origins by total number of fans

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
