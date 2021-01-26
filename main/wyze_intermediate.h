esp_err_t _http_event_handler(esp_http_client_event_t *evt);
static void wifi_event_handler(void* arg, esp_event_base_t event_base, int32_t event_id, void* event_data);
void wifi_init_sta(void);
esp_err_t handleRoot(httpd_req_t *req);
esp_err_t handleFlash(httpd_req_t *req);
esp_err_t handleBackup(httpd_req_t *req);
esp_err_t handleUndo(httpd_req_t *req);
void stop_webserver(httpd_handle_t server);
httpd_handle_t start_webserver(void);
static void disconnect_handler(void* arg, esp_event_base_t event_base, int32_t event_id, void* event_data);
static int do_flash(const char * url);
char build_ota_url(char * ipstr, char * ota_full);
void app_main();
uint32_t user_rf_cal_sector_set(void);