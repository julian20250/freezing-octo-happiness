
@echo Hola, hice este programa para que pod is saber cu ntas copias deb‚is sacarde cada ^
examen dependiendo de la cantidad de estudiantes.
@echo.
@set /p a=Ahora, decidme. Cu ntos estudiantes son? 
@set /p b=Y, Cu ntos parciales preparasteis?  
@set /a c=%a%%%b%
@set /a f=%a%/%b%
@echo.
@set d=0
@set /a e=%f%+1
@setlocal EnableDelayedExpansion
@if not %c% == 0 (
@for /l %%t in (1 1 %c%) do @( 
	@set /a d=!d!+1
	@echo Al examen !d! le corresponden %e% copias.
)
)
@set /a h=%b%-%c%
@setlocal EnableDelayedExpansion
@for /l %%u in (1 1 %h%) do @(
	@set /a d=!d!+1
	@echo Al examen !d! le corresponden %f% copias.
)
@pause
:Referencias
:- Tildes: http://www.taringa.net/post/offtopic/17225473/Acentos-en-programacion-Batch.html
