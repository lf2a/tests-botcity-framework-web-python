:: Tempo total da ultima execução completa 35 min 53 sec
:: Leva aproximadamente 5min para execução de cada teste

call pytest.exe --browser=chrome --html=html/chrome-report.html
call pytest.exe --browser=firefox --html=html/firefox-report.html
call pytest.exe --browser=edge --html=html/edge-report.html

call pytest.exe --headless --browser=chrome --html=html/chrome-headless-report.html
call pytest.exe --headless --browser=firefox --html=html/firefox-headless-report.html
call pytest.exe --headless --browser=edge --html=html/edge-headless-report.html
