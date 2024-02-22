WITH WinningProducers AS (
    SELECT
        producers,
        year,
        LAG(year) OVER (PARTITION BY producers ORDER BY year) AS prev_win_year
    FROM
        movies
    WHERE
        winner = TRUE
)
SELECT
    producers,
    year AS win_year,
    prev_win_year,
    year - prev_win_year AS interval
FROM
    WinningProducers
WHERE
    prev_win_year IS NOT NULL
ORDER BY
    interval, year;