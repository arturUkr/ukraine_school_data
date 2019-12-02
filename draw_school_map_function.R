


create_map <-
  function(
    file_name,
    coord_center
  ) {
    
    data <- 
      read_xlsx(path = file_name)
    
    circle_palette <-
      colorQuantile(
        palette = "Spectral", ##scico(10, palette = 'roma'),
        probs = seq(0, 1, length.out = 10),
        domain = data$count_student,
        reverse = TRUE
      )
    
    data %>% 
      leaflet() %>% 
      addTiles() %>%
      # addProviderTiles(providers$CartoDB.DarkMatter) %>%
      # addProviderTiles(providers$CartoDB.Positron) %>%
      # setView(lng = coord_center[1], lat = coord_center[2], zoom = 10) %>% 
      addCircleMarkers(
        lng         = ~school_lng,
        lat         = ~school_lat,
        radius      = ~count_student / 100,
        # color       = ~circle_palette(count_student),
        popup       = ~glue("{school_name}, {city_name}, {street_name}, к-сть учнів - {count_student}"),
        weight      = 1,
        fillOpacity = 0.4
      )
    
  }

# create_map(here::here("for_r", "dnipro_school_coord.xlsx"), c(35.046918, 48.481173))
# create_map(here::here("for_r", "kharkiv_school_coord.xlsx"), c(36.252172, 49.986561))
# create_map(here::here("for_r", "odesa_school_coord.xlsx"), c(30.725512, 46.455629))
# create_map(here::hCere("for_r", "lviv_school_coord.xlsx"), c(24.026310, 49.843075))
# create_map(here::here("for_r", "zapor_rig_school_coord.xlsx"), c(24.026310, 49.843075))
# create_map(here::here("for_r", "c2_school_coord.xlsx"), c(24.026310, 49.843075))
# create_map(here::here("for_r", "c3_school_coord.xlsx"), c(24.026310, 49.843075))
create_map(here::here("for_r", "c4_school_coord.xlsx"), c(24.026310, 49.843075))





# load schools
df_city_school <- 
  fs::dir_ls("for_r", regexp = "for_r\\/[^~]*xlsx") %>% 
  here::here() %>% 
  map_dfr(read_xlsx)

# df_city_school %>% 
#   writexl::write_xlsx("D:/R_project/operation_on_map/00_data/01_school_data/shool_data.xlsx")



city_school_palette <-
  colorQuantile(
    palette = "Spectral", ##scico(10, palette = 'roma'),
    probs = seq(0, 1, length.out = 10),
    domain = df_city_school$count_student,
    reverse = TRUE
  )


df_city_school %>% 
  leaflet() %>% 
  # addTiles() %>%
  addProviderTiles(providers$OpenStreetMap, group  = "osm") %>% 
  addProviderTiles(providers$CartoDB.Positron, group  = "light") %>%
  addProviderTiles(providers$CartoDB.DarkMatter, group  = "dark") %>%
  # setView(lng = coord_center[1], lat = coord_center[2], zoom = 10) %>% 
  addCircles(
    lng         = ~school_lng,
    lat         = ~school_lat,
    radius      = ~count_student / 4, #  / 100
    color       = ~city_school_palette(count_student),
    popup       = ~glue("{school_name}, {city_name}, {street_name}, к-сть учнів - {count_student}"),
    weight      = 1,
    fillOpacity = 0.4
  ) %>% 
  leaflet::addLayersControl(
    baseGroups = c("dark", "light", "osm"),
  ) #%>% 
  # addLegend(
  #   position = "bottomleft",
  #   pal = city_school_palette,
  #   values = ~count_student,
  #   opacity = 1,
  #   labels = quantile(df_city_school$count_student, probs = seq(0, 1, length.out = 10))
  # )

