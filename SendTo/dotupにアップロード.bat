@if not "%~0"=="%~dp0.\%~nx0" start /min cmd /c,"%~dp0.\%~nx0" %* & goto :eof
echo %*

python "C:\Users\Toshi\Dropbox\backup\dotup Auto Uploader\auto.py" %*