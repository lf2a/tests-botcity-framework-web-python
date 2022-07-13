# Tests - botcity-framework-web-python

## Run tests

`--browsers`: `[chrome, firefox, edge]`

`--headless`: run browser in headless mode.

`--html=<path>/html-file`: generate html report file.

```shell
pytest -s --headless --browser=chrome --html=html/chrome-headless-report.html
```

| Method                          |       Tested       | Comments |
|:--------------------------------|:------------------:|----------|
| `browser`                       | :heavy_check_mark: |          |
| `driver`                        | :heavy_check_mark: |          |
| `headless`                      | :heavy_check_mark: |          |
| `activate_tab()`                | :heavy_check_mark: |          |
| `add_image()`                   | :heavy_check_mark: |          |
| `backspace()`                   | :heavy_check_mark: |          |
| `browse()`                      | :heavy_check_mark: |          |
| `click()`                       | :heavy_check_mark: |          |
| `click_at()`                    | :heavy_check_mark: |          |
| `click_on()`                    | :heavy_check_mark: |          |
| `click_relative()`              | :heavy_check_mark: |          |
| `close_page()`                  | :heavy_check_mark: |          |
| `control_a()`                   | :heavy_check_mark: |          |
| `control_c()`                   | :heavy_check_mark: |          |
| `control_v()`                   | :heavy_check_mark: |          |
| `copy_to_clipboard()`           | :heavy_check_mark: |          |
| `create_tab()`                  | :heavy_check_mark: |          |
| `create_window()`               | :heavy_check_mark: |          |
| `delete()`                      | :heavy_check_mark: |          |
| `display_size()`                | :heavy_check_mark: |          |
| `double_click()`                | :heavy_check_mark: |          |
| `double_click_relative()`       | :heavy_check_mark: |          |
| `enter()`                       | :heavy_check_mark: |          |
| `enter_iframe()`                | :heavy_check_mark: |          |
| `execute_javascript()`          | :heavy_check_mark: |          |
| `find()`                        | :heavy_check_mark: |          |
| `find_all()`                    | :heavy_check_mark: |          |
| `find_element()`                | :heavy_check_mark: |          |
| `find_elements()`               | :heavy_check_mark: |          |
| `find_multiple()`               | :heavy_check_mark: |          |
| `find_text()`                   | :heavy_check_mark: |          |
| `find_until()`                  | :heavy_check_mark: |          |
| `get_clipboard()`               | :heavy_check_mark: |          |
| `get_element_coords()`          | :heavy_check_mark: |          |
| `get_element_coords_centered()` | :heavy_check_mark: |          |
| `get_image_from_map()`          | :heavy_check_mark: |          |
| `get_js_dialog()`               | :heavy_check_mark: |          |
| `get_last_element()`            | :heavy_check_mark: |          |
| `get_last_x()`                  | :heavy_check_mark: |          |
| `get_last_y()`                  | :heavy_check_mark: |          |
| `get_screen_image()`            | :heavy_check_mark: |          |
| `get_screenshot()`              | :heavy_check_mark: |          |
| `get_tabs()`                    | :heavy_check_mark: |          |
| `get_viewport_size()`           | :heavy_check_mark: |          |
| `handle_js_dialog()`            | :heavy_check_mark: |          |
| `hold_shift()`                  | :heavy_check_mark: |          |
| `kb_type()`                     | :heavy_check_mark: |          |
| `key_end()`                     | :heavy_check_mark: |          |
| `key_enter()`                   | :heavy_check_mark: |          |
| `key_esc()`                     | :heavy_check_mark: |          |
| `key_home()`                    | :heavy_check_mark: |          |
| `key_right()`                   | :heavy_check_mark: |          |
| `leave_iframe()`                | :heavy_check_mark: |          |
| `maximize_window()`             | :heavy_check_mark: |          |
| `mouse_down()`                  | :heavy_check_mark: |          |
| `mouse_move()`                  | :heavy_check_mark: |          |
| `mouse_up()`                    | :heavy_check_mark: |          |
| `move()`                        | :heavy_check_mark: |          |
| `move_random()`                 | :heavy_check_mark: |          |
| `move_relative()`               | :heavy_check_mark: |          |
| `move_to()`                     | :heavy_check_mark: |          |
| `navigate_to()`                 | :heavy_check_mark: |          |
| `page_down()`                   | :heavy_check_mark: |          |
| `page_source()`                 | :heavy_check_mark: |          |
| `page_title()`                  | :heavy_check_mark: |          |
| `page_up()`                     | :heavy_check_mark: |          |
| `paste()`                       | :heavy_check_mark: |          |
| `print_pdf()`                   | :heavy_check_mark: |          |
| `release_shift()`               | :heavy_check_mark: |          |
| `right_click()`                 | :heavy_check_mark: |          |
| `right_click_at()`              | :heavy_check_mark: |          |
| `right_click_relative()`        | :heavy_check_mark: |          |
| `save_screenshot()`             | :heavy_check_mark: |          |
| `screen_cut()`                  | :heavy_check_mark: |          |
| `screenshot()`                  | :heavy_check_mark: |          |
| `scroll_down()`                 | :heavy_check_mark: |          |
| `scroll_up()`                   | :heavy_check_mark: |          |
| `set_current_element()`         | :heavy_check_mark: |          |
| `set_file_input_element()`      | :heavy_check_mark: |          |
| `set_screen_resolution()`       | :heavy_check_mark: |          |
| `sleep()`                       | :heavy_check_mark: |          |
| `space()`                       | :heavy_check_mark: |          |
| `start_browser()`               | :heavy_check_mark: |          |
| `stop_browser()`                | :heavy_check_mark: |          |
| `tab()`                         | :heavy_check_mark: |          |
| `triple_click()`                | :heavy_check_mark: |          |
| `triple_click_relative()`       | :heavy_check_mark: |          |
| `type_down()`                   | :heavy_check_mark: |          |
| `type_keys()`                   | :heavy_check_mark: |          |
| `type_keys_with_interval()`     | :heavy_check_mark: |          |
| `type_left()`                   | :heavy_check_mark: |          |
| `type_right()`                  | :heavy_check_mark: |          |
| `type_up()`                     | :heavy_check_mark: |          |
| `wait()`                        | :heavy_check_mark: |          |
| `wait_for_downloads()`          | :heavy_check_mark: |          |
| `wait_for_file()`               | :heavy_check_mark: |          |