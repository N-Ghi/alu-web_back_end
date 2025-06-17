-- List all bands whose main style is Glam rock, ranked by their longevity (lifespan)
-- This script assumes the existence of a table named `metal_bands` with columns `origin` and `fans`.

SELECT
    band_name,
    (COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style IS NOT NULL
    AND formed IS NOT NULL
    AND (
        FIND_IN_SET('Glam rock', REPLACE(style, ', ', ',')) > 0
    )
ORDER BY
    lifespan DESC;
