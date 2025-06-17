-- List all bands whose main style is Glam rock, ranked by their longevity (lifespan)
-- This script assumes the existence of a table named `metal_bands` with columns `origin` and `fans`.

SELECT
    band_name,
    (COALESCE(
        split,
        EXTRACT(YEAR FROM CURRENT_DATE)     -- if the band hasn’t split yet, use the current year
    )
    - formed
    ) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
    AND formed IS NOT NULL
ORDER BY
    lifespan DESC;
