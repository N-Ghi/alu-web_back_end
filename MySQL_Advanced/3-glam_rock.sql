-- List all bands whose main style is Glam rock, ranked by their longevity (lifespan)
-- This script assumes the existence of a table named `metal_bands` with columns `origin` and `fans`.

SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN 2020 - COALESCE(formed, YEAR(curdate()))
        ELSE COALESCE(split, YEAR(curdate())) - COALESCE(formed, YEAR(curdate()))
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;