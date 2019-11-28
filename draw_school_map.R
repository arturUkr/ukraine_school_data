library(here)
library(readxl)
library(dplyr)
library(leaflet)
library(glue)
library(scico)


school_data <- 
  read_xlsx(here::here("for_r", "kyiv_school_coord.xlsx"))

# school_data
# A tibble: 489 x 6


circle_palette <-
  colorQuantile(
    palette = "Spectral", ##scico(10, palette = 'roma'),
    probs = seq(0, 1, length.out = 10),
    domain = school_data$count_student,
    reverse = TRUE
  )

school_data %>% 
  leaflet() %>% 
  # addTiles() %>%
  addProviderTiles(providers$CartoDB.DarkMatter) %>%
  setView(lng = 30.554273, lat = 50.439466, zoom = 10) %>% 
  addCircleMarkers(
    lng         = ~school_lng,
    lat         = ~school_lat,
    radius      = ~count_student / 100,
    color       = ~circle_palette(count_student),
    popup       = ~glue("{school_name}, {city_name}, {street_name}, к-сть учнів - {count_student}"),
    weight      = 1,
    fillOpacity = 0.4
  )


# ------------- DNIPRO

school_data_dnipro <- 
  read_xlsx(path = here::here("for_r", "dnipro_school_coord.xlsx"))

dnipro_circle_palette <-
  colorQuantile(
    palette = "Spectral", ##scico(10, palette = 'roma'),
    probs = seq(0, 1, length.out = 10),
    domain = school_data_dnipro$count_student,
    reverse = TRUE
  )

school_data_dnipro %>% 
  leaflet() %>% 
  # addTiles() %>%
  addProviderTiles(providers$CartoDB.DarkMatter) %>%
  setView(lng = 35.046918, lat = 48.481173, zoom = 10) %>% 
  addCircleMarkers(
    lng         = ~school_lng,
    lat         = ~school_lat,
    radius      = ~count_student / 100,
    color       = ~dnipro_circle_palette(count_student),
    popup       = ~glue("{school_name}, {city_name}, {street_name}, к-сть учнів - {count_student}"),
    weight      = 1,
    fillOpacity = 0.4
  )
